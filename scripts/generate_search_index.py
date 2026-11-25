#!/usr/bin/env python3
"""Extrai automaticamente LED_INFO e SYM_INFO das 9 páginas de equipamento para cte-search-index.js."""

from pathlib import Path
import html
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "cte-search-index.js"

EQUIPMENTS = [
    {
        "dir": "Robot_NAO_V6",
        "key": "nao",
        "name": "Robô NAO V6",
        "cat": "robotica",
        "color": "",
        "synonyms": "robo robot humanoide nao choregraphe ip voz portugues motores",
    },
    {
        "dir": "DJI_Avata_Drone",
        "key": "avata2",
        "name": "DJI Avata 2",
        "cat": "drones",
        "color": "teal",
        "synonyms": "drone fpv avata oculos goggles motion comando voar camara camera rth",
    },
    {
        "dir": "Meta_Quest_3_VR",
        "key": "quest3",
        "name": "Meta Quest 3 VR",
        "cat": "vr",
        "color": "purple",
        "synonyms": "oculos vr rv realidade virtual mista meta quest boundary guardian casting projetar som",
    },
    {
        "dir": "DJI_RoboMaster_TT",
        "key": "robomaster",
        "name": "DJI RoboMaster TT",
        "cat": "drones",
        "color": "teal",
        "synonyms": "drone pequeno sala aula tello robomaster python mind+ wifi wi-fi matriz led esp32",
    },
    {
        "dir": "DJI_Pocket_2_Creator",
        "key": "pocket2",
        "name": "DJI Pocket 2",
        "cat": "audiovisual",
        "color": "blue",
        "synonyms": "camara camera filmar video entrevista microfone som audio gimbal estabilizador sd mimo",
    },
    {
        "dir": "Scanner_3D_Einstar",
        "key": "einstar",
        "name": "Scanner 3D Einstar",
        "cat": "3d",
        "color": "emerald",
        "synonyms": "scanner 3d digitalizar digitalizacao impressora 3d exstar stl obj calibracao gpu tracking",
    },
    {
        "dir": "Tuxedo_AI_NAS_QNAP",
        "key": "tuxedo",
        "name": "Tuxedo AI & NAS QNAP",
        "cat": "ia-redes",
        "color": "indigo",
        "synonyms": "servidor computador estacao ia gpu cuda vram linux ollama nas qnap zfs smb ssh vm ups",
    },
    {
        "dir": "Cricut_Maker_3",
        "key": "cricut",
        "name": "Cricut Maker 3",
        "cat": "corte",
        "color": "",
        "synonyms": "cricut maker 3 impressora corte vinil htv iron-on termocolante design space tapete lamina suporte b rodinhas espelhar usb bluetooth 24v",
    },
    {
        "dir": "Promethean_ActivPanel_LX",
        "key": "activpanel",
        "name": "Promethean ActivPanel LX",
        "cat": "audiovisual",
        "color": "blue",
        "synonyms": "painel interativo quadro interativo promethean activpanel lx 65 ecra monitor tatil toque touch caneta ops ops-a android edla hdmi usb-c espelhamento screen share airplay miracast freeze standby mdm",
    },
]

# Expansões de género e sinónimos comuns para melhorar pesquisas em português do dia a dia
WORD_ALIASES = {
    "vermelho": "vermelha luz vermelha encarnado encarnada erro alerta",
    "amarelo": "amarela luz amarela laranja",
    "laranja": "amarelo amarela luz laranja",
    "verde": "luz verde",
    "azul": "luz azul",
    "branco": "branca luz branca",
    "roxo": "roxa violeta lilas luz roxa",
    "apagado": "apagada sem luz nao liga desligado desligada sem energia",
    "sem luz": "apagado apagada nao liga sem energia",
    "piscar": "pisca intermitente flash luz",
    "wi-fi": "wifi rede internet ligacao",
    "wi-fi do drone nao aparece": "sem wi-fi sem wifi rede",
    "nao aparece": "sem ligacao desapareceu",
    "desfocada": "desfocado turvo embaciado embaciada foco",
    "embaciada": "embaciado desfocado desfocada turvo",
    "tonturas": "enjoo nauseas mal estar",
    "bloqueado": "bloqueada travou encravou congelou nao responde",
    "bloqueados": "bloqueado travou encravou ecra preto nao liga",
    "ecra preto": "nao liga sem imagem bloqueado sem sinal",
    "sem sinal": "sem imagem ecra preto hdmi usb-c entrada fonte",
    "sem imagem": "sem sinal ecra preto hdmi usb-c entrada fonte",
    "toque": "touch tatil caneta nao responde",
    "freeze": "congelado congelada parado parada imagem parada",
    "congelado": "freeze parado bloqueado imagem parada",
    "screen share": "espelhamento airplay miracast projetar partilhar ecra sem fios",
    "nao liga": "desligado sem energia bateria botao interruptor",
    "sem som": "sem audio mudo microfone volume colunas",
    "microfone": "mic som audio voz gravar",
    "sobreaquecimento": "quente aquece temperatura ventoinha",
    "aquece": "quente sobreaquecimento temperatura",
    "bateria": "carregar carregador carga descarregado",
    "tapete": "base aderente folha cartolina smart material",
    "vinil": "autocolante htv iron-on termocolante decalque",
    "lamina": "laminas corte suporte b fresa rasga nao corta",
    "espelhar": "invertido contrario espelho mirror htv termocolante",
    "htv": "termocolante iron-on camisola t-shirt ferro espelhar",
}

ENTRY_RE = re.compile(
    r'(\w+):\s*\{\s*'
    r'cls:\s*"([^"]*)",\s*'
    r'title:\s*"((?:\\.|[^"\\])*)",\s*'
    r'(meaning|cause):\s*"((?:\\.|[^"\\])*)",\s*'
    r'action:\s*"((?:\\.|[^"\\])*)"\s*'
    r'\}',
    re.S,
)

LED_BTN_RE = re.compile(
    r'<button[^>]*data-led="([^"]+)"[^>]*>(.*?)</button>',
    re.S,
)

SYM_BTN_RE = re.compile(
    r'<button[^>]*data-sym="([^"]+)"[^>]*>(.*?)</button>',
    re.S,
)


def normalize_text(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value or "")
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", stripped.lower()).strip()


def unescape_js_str(value: str) -> str:
    return value.replace('\\"', '"').replace("\\'", "'").replace("\\n", " ")


def strip_html(value: str) -> str:
    clean = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(clean)).strip()


def truncate(text: str, limit: int = 155) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return cut + "…"


def dedupe_tokens(norm_text: str) -> str:
    seen: set[str] = set()
    out: list[str] = []
    for tok in norm_text.split():
        if tok not in seen:
            seen.add(tok)
            out.append(tok)
    return " ".join(out)


def expand_aliases(norm_text: str) -> str:
    extras = []
    for trigger, expansion in WORD_ALIASES.items():
        if trigger in norm_text:
            extras.append(expansion)
    return " ".join(extras)


def parse_equipment(eq: dict) -> list[dict]:
    html_path = ROOT / eq["dir"] / "index.html"
    content = html_path.read_text(encoding="utf-8")

    # Extrair botões LED (rótulo, classe led-pat-* e descrição)
    led_meta: dict[str, dict] = {}
    for m in LED_BTN_RE.finditer(content):
        full_tag = m.group(0)
        key = m.group(1)
        inner = m.group(2)
        pat_m = re.search(r'\b(led-pat-[a-z0-9-]+)\b', inner)
        desc_m = re.search(r'data-led-desc="([^"]+)"', full_tag)
        led_meta[key] = {
            "label": strip_html(inner),
            "ledClass": pat_m.group(1) if pat_m else "",
            "ledDesc": html.unescape(desc_m.group(1)) if desc_m else strip_html(inner),
        }

    # Extrair botões de sintoma
    sym_labels: dict[str, str] = {}
    for m in SYM_BTN_RE.finditer(content):
        sym_labels[m.group(1)] = strip_html(m.group(2))

    items: list[dict] = []

    # Bloco LED_INFO
    led_block_m = re.search(r"var\s+LED_INFO\s*=\s*\{(.*?)\n  \};", content, re.S)
    if led_block_m:
        for m in ENTRY_RE.finditer(led_block_m.group(1)):
            key = m.group(1)
            severity = m.group(2)
            title = strip_html(unescape_js_str(m.group(3)))
            meaning = strip_html(unescape_js_str(m.group(5)))
            action = strip_html(unescape_js_str(m.group(6)))
            meta = led_meta.get(key, {})
            label = meta.get("label") or title
            led_desc = meta.get("ledDesc") or label

            base_norm = normalize_text(
                f"{eq['name']} {eq['synonyms']} led luz {label} {led_desc} {title} {meaning} {action}"
            )
            search_text = dedupe_tokens(normalize_text(f"{base_norm} {expand_aliases(base_norm)}"))
            title_norm = dedupe_tokens(normalize_text(f"led luz {label} {led_desc} {title} {expand_aliases(normalize_text(label + ' ' + title))}"))

            items.append({
                "equip": eq["key"],
                "equipName": eq["name"],
                "cat": eq["cat"],
                "color": eq["color"],
                "kind": "led",
                "key": key,
                "label": label,
                "title": title,
                "snippet": truncate(f"{meaning} — {action}"),
                "severity": severity,
                "ledClass": meta.get("ledClass", ""),
                "ledDesc": led_desc,
                "url": f"{eq['dir']}/index.html?led={key}#diagnostico",
                "titleNorm": title_norm,
                "searchText": search_text,
            })

    # Bloco SYM_INFO
    sym_block_m = re.search(r"var\s+SYM_INFO\s*=\s*\{(.*?)\n  \};", content, re.S)
    if sym_block_m:
        for m in ENTRY_RE.finditer(sym_block_m.group(1)):
            key = m.group(1)
            severity = m.group(2)
            title = strip_html(unescape_js_str(m.group(3)))
            cause = strip_html(unescape_js_str(m.group(5)))
            action = strip_html(unescape_js_str(m.group(6)))
            label = sym_labels.get(key) or title

            base_norm = normalize_text(
                f"{eq['name']} {eq['synonyms']} sintoma problema avaria {label} {title} {cause} {action}"
            )
            search_text = dedupe_tokens(normalize_text(f"{base_norm} {expand_aliases(base_norm)}"))
            title_norm = dedupe_tokens(normalize_text(f"{label} {title} {expand_aliases(normalize_text(label + ' ' + title))}"))

            items.append({
                "equip": eq["key"],
                "equipName": eq["name"],
                "cat": eq["cat"],
                "color": eq["color"],
                "kind": "sym",
                "key": key,
                "label": label,
                "title": title,
                "snippet": truncate(action),
                "severity": severity,
                "ledClass": "",
                "ledDesc": "",
                "url": f"{eq['dir']}/index.html?sym={key}#diagnostico",
                "titleNorm": title_norm,
                "searchText": search_text,
            })

    return items


def generate_index() -> list[dict]:
    all_items: list[dict] = []
    for eq in EQUIPMENTS:
        all_items.extend(parse_equipment(eq))

    header = (
        "/**\n"
        " * Índice global de diagnóstico (LEDs e sintomas) dos 9 equipamentos do CTE.\n"
        " * Gerado automaticamente por scripts/generate_search_index.py — não editar manualmente.\n"
        " */\n"
        "window.CTE_SEARCH_INDEX = "
    )
    payload = json.dumps(all_items, ensure_ascii=False, separators=(",", ":"))
    OUTPUT.write_text(f"{header}{payload};\n", encoding="utf-8")
    return all_items


def main() -> int:
    items = generate_index()
    leds = sum(1 for x in items if x["kind"] == "led")
    syms = sum(1 for x in items if x["kind"] == "sym")
    print(f"Índice gerado em {OUTPUT.name}: {len(items)} entradas ({leds} LEDs + {syms} sintomas).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
