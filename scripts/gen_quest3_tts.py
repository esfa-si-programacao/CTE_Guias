#!/usr/bin/env python3
"""Gera narração neural em Português Europeu (pt-PT-RaquelNeural) + legendas VTT para o demo Meta Quest 3."""

import asyncio
import json
from pathlib import Path
import edge_tts

ROOT = Path(__file__).resolve().parent.parent
DEMO_DIR = ROOT / "Meta_Quest_3_VR" / "demo_video"
AUDIO_DIR = DEMO_DIR / "audio"

VOICE = "pt-PT-RaquelNeural"
RATE = "+0%"

SCENES = [
    {
        "id": "scene_01",
        "img": "scene_01_sun.png",
        "step": "Passo 1 de 6",
        "title": "ZERO sol nas lentes",
        "title_color": "#B91C1C",
        "text": "Antes de abrir a mala dos Meta Quest 3, afaste-se das janelas. A luz solar direta queima as lentes internas em poucos segundos.",
    },
    {
        "id": "scene_02",
        "img": "scene_02_space.png",
        "step": "Passo 2 de 6",
        "title": "Espaço 2 × 2 m + fitas nos pulsos",
        "title_color": "#166874",
        "text": "Liberte um espaço de dois por dois metros sem mesas nem obstáculos, e aperte sempre as fitas dos dois comandos nos pulsos.",
    },
    {
        "id": "scene_03",
        "img": "scene_03_power_ipd.png",
        "step": "Passo 3 de 6",
        "title": "Ligar (3 s) e focar as lentes",
        "title_color": "#1F2A36",
        "text": "Prima o botão lateral esquerdo durante três segundos até acender o LED branco. Ajuste as fitas e rode a roda inferior esquerda até o texto ficar nítido.",
    },
    {
        "id": "scene_04",
        "img": "scene_04_passthrough.png",
        "step": "Passo 4 de 6",
        "title": "2 toques = Ver a sala real",
        "title_color": "#C4590E",
        "text": "Precisa de ver à sua volta sem tirar os óculos? Dê dois toques suaves na lateral do visor para ativar a vista real a cores.",
    },
    {
        "id": "scene_05",
        "img": "scene_05_recenter.png",
        "step": "Passo 5 de 6",
        "title": "Botão Meta (2 s) e Limite",
        "title_color": "#6C3483",
        "text": "Para recentrar o menu à sua frente, mantenha premido o botão Meta no comando direito durante dois segundos, e confirme sempre o Limite de segurança.",
    },
    {
        "id": "scene_06",
        "img": "scene_06_return.png",
        "step": "Passo 6 de 6",
        "title": "Desligar, limpar e proteger",
        "title_color": "#1E8449",
        "text": "No final da aula, desligue totalmente os óculos, limpe as lentes só com microfibra seca, coloque o protetor opaco e entregue a mala completa no CTE.",
    },
]


def fmt_vtt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, rem = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{rem:03d}"


def chunk_words(words: list[dict], max_words: int = 5, max_chars: int = 34) -> list[dict]:
    """Agrupa palavras com timestamps em pequenas frases legíveis (estilo vídeo do NAO)."""
    chunks = []
    buf = []
    for w in words:
        cand = " ".join([x["text"] for x in buf] + [w["text"]])
        if buf and (len(buf) >= max_words or len(cand) > max_chars):
            chunks.append({
                "start": buf[0]["start"],
                "end": buf[-1]["end"],
                "text": " ".join(x["text"] for x in buf),
            })
            buf = [w]
        else:
            buf.append(w)
            if w["text"].endswith((".", "?", "!", ",")) and len(buf) >= 3:
                chunks.append({
                    "start": buf[0]["start"],
                    "end": buf[-1]["end"],
                    "text": " ".join(x["text"] for x in buf),
                })
                buf = []
    if buf:
        chunks.append({
            "start": buf[0]["start"],
            "end": buf[-1]["end"],
            "text": " ".join(x["text"] for x in buf),
        })
    return chunks


async def synth_scene(scene: dict) -> dict:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    mp3_path = AUDIO_DIR / f"{scene['id']}.mp3"
    comm = edge_tts.Communicate(scene["text"], VOICE, rate=RATE, boundary="WordBoundary")
    words = []
    with mp3_path.open("wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 10_000_000.0
                dur = chunk["duration"] / 10_000_000.0
                words.append({"start": start, "end": start + dur, "text": chunk["text"]})

    # Garantir duração mínima com pequeno respiro final
    speech_end = words[-1]["end"] if words else 8.0
    duration = round(speech_end + 0.65, 3)
    captions = chunk_words(words) if words else [{"start": 0.1, "end": speech_end, "text": scene["text"]}]
    return {
        **scene,
        "audio": mp3_path.name,
        "duration": duration,
        "captions": captions,
    }


async def main() -> None:
    meta = []
    offset = 0.0
    vtt_lines = ["WEBVTT", ""]
    cue_idx = 1

    for scene in SCENES:
        info = await synth_scene(scene)
        info["global_start"] = round(offset, 3)
        meta.append(info)

        # Escrever legendas VTT sincronizadas com o vídeo completo
        for cap in info["captions"]:
            t0 = offset + cap["start"]
            t1 = offset + cap["end"] + 0.15
            vtt_lines.append(str(cue_idx))
            vtt_lines.append(f"{fmt_vtt_time(t0)} --> {fmt_vtt_time(t1)}")
            vtt_lines.append(cap["text"])
            vtt_lines.append("")
            cue_idx += 1

        offset += info["duration"]
        print(f"OK {scene['id']}: {info['duration']:.2f}s ({len(info['captions'])} legendas)")

    out_json = DEMO_DIR / "audio_timings.json"
    out_json.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    out_vtt = DEMO_DIR / "Como_Usar_os_Meta_Quest_3.vtt"
    out_vtt.write_text("\n".join(vtt_lines), encoding="utf-8")

    print(f"Total áudio: {offset:.2f}s | Guardado {out_json.name} e {out_vtt.name}")


if __name__ == "__main__":
    asyncio.run(main())
