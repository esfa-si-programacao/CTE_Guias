#!/usr/bin/env python3
"""Monta o vídeo vertical MP4 (720×1280, 30 fps) e gera cópias WebP leves das ilustrações (100% offline)."""

import json
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent.parent
DEMO_DIR = ROOT / "Meta_Quest_3_VR" / "demo_video"
IMG_DIR = DEMO_DIR / "imgs"
WEBP_DIR = DEMO_DIR / "webp"
AUDIO_DIR = DEMO_DIR / "audio"
TIMINGS_JSON = DEMO_DIR / "audio_timings.json"
OUT_MP4 = DEMO_DIR / "Como_Usar_os_Meta_Quest_3.mp4"

W, H = 720, 1280
FPS = 30
BG = (247, 244, 236)  # #F7F4EC papel creme caderno técnico
PILL_BG = (232, 226, 213)  # #E8E2D5 estilo legenda do vídeo NAO
OUTRO_SEC = 2.4


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def prepare_canvas(img_path: Path) -> Image.Image:
    """Ajusta a ilustração gerada por IA a um quadrado/vertical limpo sobre papel #F7F4EC e exporta WebP."""
    im = Image.open(img_path).convert("RGB")

    # Exportar versão WebP leve para a Opção 3 (player interativo HTML)
    WEBP_DIR.mkdir(parents=True, exist_ok=True)
    webp_out = WEBP_DIR / (img_path.stem + ".webp")
    preview = im.copy()
    preview.thumbnail((680, 1200), Image.Resampling.LANCZOS)
    preview.save(webp_out, format="WEBP", quality=82, method=6)

    # Preparar base de alta resolução para efeito Ken Burns suave (1.00 -> 1.05)
    target_w, target_h = int(W * 1.08), int(H * 1.08)
    src_ratio = im.width / im.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:
        new_h = target_h
        new_w = int(round(new_h * src_ratio))
    else:
        new_w = target_w
        new_h = int(round(new_w / src_ratio))
    resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    lines = []
    cur = []
    for w in words:
        test = " ".join(cur + [w])
        bbox = draw.textbbox((0, 0), test, font=font)
        if cur and (bbox[2] - bbox[0]) > max_w:
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_frame(
    base_img: Image.Image,
    scene: dict,
    local_t: float,
    total_t: float,
    video_progress: float,
    fonts: dict,
) -> Image.Image:
    # Suave efeito Ken Burns (zoom 1.00 -> 1.045)
    frac = min(1.0, max(0.0, local_t / max(total_t, 0.1)))
    zoom = 1.0 + 0.045 * frac
    crop_w = int(round(base_img.width / zoom))
    crop_h = int(round(base_img.height / zoom))
    x0 = (base_img.width - crop_w) // 2
    y0 = (base_img.height - crop_h) // 2
    frame = base_img.crop((x0, y0, x0 + crop_w, y0 + crop_h)).resize((W, H), Image.Resampling.BILINEAR)

    # Gradiente suave nas bandas superior e inferior para leitura perfeita de títulos e legendas
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(230):
        alpha = int(235 * (1.0 - (y / 230.0) ** 1.6))
        od.line([(0, y), (W, y)], fill=(BG[0], BG[1], BG[2], alpha))
    for y in range(250):
        alpha = int(240 * ((y / 250.0) ** 1.5))
        yy = H - 250 + y
        od.line([(0, yy), (W, yy)], fill=(BG[0], BG[1], BG[2], alpha))

    frame = Image.alpha_composite(frame.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(frame)

    # Barra de progresso discreta no topo
    draw.rectangle([(0, 0), (W, 7)], fill=(224, 218, 204))
    draw.rectangle([(0, 0), (int(W * video_progress), 7)], fill=(108, 52, 131))

    # Pill do passo (ex.: Passo 1 de 6 · Meta Quest 3 VR)
    pill_text = f"{scene['step']}  ·  Meta Quest 3 VR"
    pb = draw.textbbox((0, 0), pill_text, font=fonts["step"])
    pw = pb[2] - pb[0] + 34
    ph = pb[3] - pb[1] + 16
    px = (W - pw) // 2
    py = 40
    draw.rounded_rectangle([(px, py), (px + pw, py + ph)], radius=20, fill=(235, 229, 217), outline=(206, 198, 182), width=1)
    draw.text((px + 17, py + 7), pill_text, font=fonts["step"], fill=(74, 85, 96))

    # Título principal da cena
    title_rgb = hex_to_rgb(scene["title_color"])
    title_lines = wrap_text(draw, scene["title"], fonts["title"], W - 80)
    ty = py + ph + 24
    for line in title_lines:
        lb = draw.textbbox((0, 0), line, font=fonts["title"])
        lw = lb[2] - lb[0]
        draw.text(((W - lw) // 2, ty), line, font=fonts["title"], fill=title_rgb)
        ty += (lb[3] - lb[1]) + 10

    # Legenda inferior sincronizada (estilo caixa de papel do vídeo NAO)
    active_cap = ""
    for cap in scene["captions"]:
        if cap["start"] - 0.05 <= local_t <= cap["end"] + 0.25:
            active_cap = cap["text"]
            break

    if active_cap:
        cap_lines = wrap_text(draw, active_cap, fonts["cap"], W - 120)
        line_h = 44
        block_h = len(cap_lines) * line_h + 24
        max_lw = max((draw.textbbox((0, 0), ln, font=fonts["cap"])[2] for ln in cap_lines), default=200)
        box_w = min(W - 68, max_lw + 48)
        bx = (W - box_w) // 2
        by = H - 110 - block_h // 2
        draw.rounded_rectangle([(bx, by), (bx + box_w, by + block_h)], radius=14, fill=PILL_BG, outline=(210, 202, 186), width=1)
        cy = by + 13
        for ln in cap_lines:
            lb = draw.textbbox((0, 0), ln, font=fonts["cap"])
            lw = lb[2] - lb[0]
            draw.text(((W - lw) // 2, cy), ln, font=fonts["cap"], fill=(31, 42, 54))
            cy += line_h

    # Assinatura subtil no canto inferior direito
    sig = "CTE Informático · Escolas de Mangualde"
    sb = draw.textbbox((0, 0), sig, font=fonts["sig"])
    draw.text((W - (sb[2] - sb[0]) - 26, H - 36), sig, font=fonts["sig"], fill=(138, 132, 120))

    return frame


def make_outro_frame(fonts: dict) -> Image.Image:
    im = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(im)
    draw.rectangle([(0, 0), (W, 7)], fill=(108, 52, 131))

    logo_path = ROOT / "logo_escolas_mangualde.png"
    y_cursor = 430
    if logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((320, 120), Image.Resampling.LANCZOS)
        bg_card = Image.new("RGB", (logo.width + 44, logo.height + 28), (255, 255, 255))
        im.paste(bg_card, ((W - bg_card.width) // 2, y_cursor))
        im.paste(logo, ((W - logo.width) // 2, y_cursor + 14), logo)
        y_cursor += bg_card.height + 46

    lines = [
        ("Meta Quest 3 VR", fonts["title"], (108, 52, 131)),
        ("Pronto para a aula!", fonts["outro_sub"], (31, 42, 54)),
        ("Próximo passo: tirar a Carta de Condução VR", fonts["step"], (91, 102, 114)),
    ]
    for txt, fnt, col in lines:
        b = draw.textbbox((0, 0), txt, font=fnt)
        draw.text(((W - (b[2] - b[0])) // 2, y_cursor), txt, font=fnt, fill=col)
        y_cursor += (b[3] - b[1]) + 22
    return im


def concat_audio(ffmpeg_exe: str, scenes: list[dict], out_wav: Path) -> None:
    """Concatena os 6 clips MP3 com o padding exato de cada cena + silêncio do ecrã final."""
    inputs = []
    filters = []
    for idx, sc in enumerate(scenes):
        inputs.extend(["-i", str(AUDIO_DIR / sc["audio"])])
        dur = sc["duration"]
        filters.append(f"[{idx}:a]apad=whole_dur={dur:.3f},atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[a{idx}]")

    # Silêncio final para o outro
    n = len(scenes)
    concat_in = "".join(f"[a{i}]" for i in range(n))
    filter_complex = ";".join(filters) + f";{concat_in}concat=n={n}:v=0:a=1,apad=pad_dur={OUTRO_SEC:.2f}[aout]"

    cmd = [
        ffmpeg_exe, "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[aout]",
        "-ar", "44100", "-ac", "1",
        str(out_wav),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main() -> int:
    if not TIMINGS_JSON.exists():
        print("ERRO: execute primeiro scripts/gen_quest3_tts.py", file=sys.stderr)
        return 1

    scenes = json.loads(TIMINGS_JSON.read_text(encoding="utf-8"))
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    fonts = {
        "step": load_font(22, bold=True),
        "title": load_font(42, bold=True),
        "cap": load_font(32, bold=False),
        "sig": load_font(18, bold=False),
        "outro_sub": load_font(34, bold=True),
    }

    # Preparar imagens + exportar WebPs leves para Opção 3
    bases = []
    for sc in scenes:
        p = IMG_DIR / sc["img"]
        if not p.exists():
            print(f"ERRO: imagem em falta: {p}", file=sys.stderr)
            return 1
        bases.append(prepare_canvas(p))

    # Concatenar áudio sincronizado
    full_audio = AUDIO_DIR / "full_track.wav"
    concat_audio(ffmpeg_exe, scenes, full_audio)

    total_video_sec = sum(sc["duration"] for sc in scenes) + OUTRO_SEC
    outro_frame = make_outro_frame(fonts)

    # Abrir pipe de vídeo raw RGB diretamente para ffmpeg (H.264 + AAC, faststart)
    cmd = [
        ffmpeg_exe, "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}",
        "-r", str(FPS),
        "-i", "-",
        "-i", str(full_audio),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "24",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        "-shortest",
        str(OUT_MP4),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    fade_frames = int(round(0.32 * FPS))
    prev_last_frame = None
    elapsed_global = 0.0

    try:
        for idx, sc in enumerate(scenes):
            n_frames = int(round(sc["duration"] * FPS))
            base = bases[idx]
            for f in range(n_frames):
                local_t = f / FPS
                prog = min(1.0, (elapsed_global + local_t) / total_video_sec)
                frame = draw_frame(base, sc, local_t, sc["duration"], prog, fonts)
                if prev_last_frame is not None and f < fade_frames:
                    alpha = (f + 1) / (fade_frames + 1)
                    frame = Image.blend(prev_last_frame, frame, alpha)
                proc.stdin.write(frame.tobytes())
                if f == n_frames - 1:
                    prev_last_frame = frame
            elapsed_global += sc["duration"]
            print(f"Renderizada {sc['id']} ({n_frames} frames)")

        outro_frames = int(round(OUTRO_SEC * FPS))
        for f in range(outro_frames):
            frame = outro_frame
            if prev_last_frame is not None and f < fade_frames:
                alpha = (f + 1) / (fade_frames + 1)
                frame = Image.blend(prev_last_frame, outro_frame, alpha)
            proc.stdin.write(frame.tobytes())

        proc.stdin.close()
        stderr = proc.stderr.read().decode("utf-8", errors="replace")
        ret = proc.wait()
        if ret != 0:
            print("ERRO ffmpeg:", stderr, file=sys.stderr)
            return ret
    finally:
        if full_audio.exists():
            full_audio.unlink()

    size_mb = OUT_MP4.stat().st_size / (1024 * 1024)
    webp_kb = sum(p.stat().st_size for p in WEBP_DIR.glob("*.webp")) / 1024
    print(f"OK! Vídeo MP4 criado: {OUT_MP4.name} ({size_mb:.2f} MB, {total_video_sec:.1f}s)")
    print(f"OK! 6 ilustrações WebP leves em webp/: {webp_kb:.1f} KB no total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
