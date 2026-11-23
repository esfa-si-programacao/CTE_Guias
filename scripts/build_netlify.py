#!/usr/bin/env python3
"""Prepara a pasta limpa `_site/` para publicação na Netlify e valida ligações locais."""

from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"

EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".vscode",
    "_site",
    "_interno",
    "demo_video",
    "scripts",
    "outros",
    "node_modules",
    "__pycache__",
}

EXCLUDED_EXTENSIONS_ANYWHERE = {
    ".xlsx",
    ".xls",
    ".xlsm",
    ".tmp",
    ".bak",
    ".pyc",
}

EXCLUDED_ROOT_FILES = {
    "A_fazer.md",
    "README.md",
    "site.txt",
    "netlify.toml",
    ".gitignore",
    ".gitattributes",
    ".htaccess",
}

EXCLUDED_ROOT_EXTENSIONS = {
    ".docx",
    ".pptx",
    ".md",
}

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"', re.IGNORECASE)
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#")


def should_skip_file(rel: Path) -> bool:
    name = rel.name
    suffix = rel.suffix.lower()
    if name.startswith("~$"):
        return True
    if suffix in EXCLUDED_EXTENSIONS_ANYWHERE:
        return True
    if len(rel.parts) == 1:
        if name in EXCLUDED_ROOT_FILES or suffix in EXCLUDED_ROOT_EXTENSIONS:
            return True
    return False


def build_site() -> tuple[int, int]:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    file_count = 0
    total_bytes = 0

    for item in ROOT.rglob("*"):
        rel = item.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if item.is_dir():
            continue
        if should_skip_file(rel):
            continue

        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, dest)
        file_count += 1
        total_bytes += item.stat().st_size

    return file_count, total_bytes


def verify_links() -> list[str]:
    broken: list[str] = []
    for html_file in sorted(OUT.rglob("*.html")):
        raw = html_file.read_text(encoding="utf-8", errors="replace")
        live = COMMENT_RE.sub("", raw)
        for match in ATTR_RE.finditer(live):
            ref = match.group(1).strip()
            if not ref or ref.startswith(EXTERNAL_PREFIXES):
                continue
            path_part = ref.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            decoded = unquote(path_part)
            if decoded.startswith("/"):
                target = OUT / decoded.lstrip("/")
            else:
                target = (html_file.parent / decoded).resolve()
            if not target.exists():
                rel_html = html_file.relative_to(OUT).as_posix()
                broken.append(f"{rel_html} -> {ref}")
    return broken


def main() -> int:
    # Atualizar índice global de sintomas antes de copiar para _site/
    try:
        import generate_search_index
        items = generate_search_index.generate_index()
        print(f"Índice de diagnóstico atualizado: {len(items)} entradas.")
    except Exception as exc:
        print(f"AVISO: não foi possível regenerar cte-search-index.js: {exc}", file=sys.stderr)

    count, total_bytes = build_site()
    broken = verify_links()
    size_mb = total_bytes / (1024 * 1024)
    print(f"Build Netlify concluído: {count} ficheiros ({size_mb:.2f} MB) em _site/")
    if broken:
        print("ERRO: Ligações locais partidas encontradas em _site/:", file=sys.stderr)
        for entry in broken:
            print(f"  - {entry}", file=sys.stderr)
        return 1
    print("Verificação de ligações locais: 0 erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
