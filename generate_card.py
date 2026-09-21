#!/usr/bin/env python3
"""Render the terminal-style profile card in dark and light variants.

One spec, two SVGs. Edit CARD below and re-run:  python generate_card.py
"""

from html import escape

FONT = "'JetBrains Mono', 'SFMono-Regular', 'Consolas', 'Menlo', 'DejaVu Sans Mono', monospace"
FONT_SIZE = 13.0
CHAR_W = FONT_SIZE * 0.6
LINE_H = 19.0
PAD_X = 24.0
TITLEBAR_H = 34.0
PAD_TOP = 16.0
PAD_BOTTOM = 18.0
LABEL_W = 11

THEMES = {
    "dark_mode.svg": {
        "bg": "#0d1117", "chrome": "#161b22", "border": "#30363d",
        "text": "#c9d1d9", "muted": "#8b949e", "prompt": "#3fb950",
        "cmd": "#58a6ff", "label": "#a371f7", "accent": "#d29922",
        "ok": "#3fb950", "dot1": "#f85149", "dot2": "#d29922", "dot3": "#3fb950",
    },
    "light_mode.svg": {
        "bg": "#ffffff", "chrome": "#f6f8fa", "border": "#d0d7de",
        "text": "#1f2328", "muted": "#59636e", "prompt": "#1a7f37",
        "cmd": "#0969da", "label": "#8250df", "accent": "#9a6700",
        "ok": "#1a7f37", "dot1": "#cf222e", "dot2": "#9a6700", "dot3": "#1a7f37",
    },
}

TITLE = "aditya@adityamore.dev — ~/profile"


def cmd(text):
    return [("$ ", "prompt"), (text, "cmd")]


def kv(label, value, tail=None):
    segs = [(label.ljust(LABEL_W), "label"), (value, "text")]
    if tail:
        segs.append((tail, "muted"))
    return segs


# Each entry is either None (blank line) or a list of (text, color-role) runs.
CARD = [
    cmd("whoami"),
    [("Aditya More", "text"), ("  ·  ", "muted"),
     ("Data Scientist & Machine Learning Engineer", "accent"),
     ("  ·  Pittsburgh, PA", "muted")],
    None,
    cmd("cat profile.yaml"),
    kv("research", "LLM agents & human-behavior simulation", " — School of Computing, Clemson"),
    kv("education", "M.S. Computer Science, Clemson University", " — Data Science & Informatics, Dec 2025"),
    kv("focus", "LLMs · RAG · Deep Learning · Computer Vision · AI Security · MLOps"),
    kv("open_to", "AI Engineer · ML Engineer · Data Scientist", " — US, open to relocation"),
    None,
    cmd("cat stack.toml"),
    kv("languages", "Python · TypeScript · SQL · C++"),
    kv("ml", "PyTorch · TensorFlow · scikit-learn · Transformers · OpenCV · pandas"),
    kv("llm", "OpenAI Responses & Embeddings · retrieval pipelines · eval harnesses"),
    kv("web", "Next.js 16 · React 19 · Flask · FastAPI · Node 24"),
    kv("cloud", "AWS Amplify · DynamoDB · S3 Vectors · Lightsail · Docker · GitHub Actions"),
    None,
    cmd("cat live.hosts"),
    [("adityamore.dev".ljust(26), "ok"), ("portfolio + BB-8 RAG co-pilot", "muted")],
    [("neurallog.adityamore.dev".ljust(26), "ok"), ("Neural Log — activity tracking + XP ledger", "muted")],
    [("game.adityamore.dev".ljust(26), "ok"), ("FIFA World Cup 2026 — prediction platform", "muted")],
    None,
    [("$ ", "prompt"), ("_", "text")],
]


def render(theme):
    cols = max(sum(len(t) for t, _ in line) for line in CARD if line)
    cols = max(cols, len(TITLE) + 12)
    width = round(cols * CHAR_W + PAD_X * 2, 1)
    height = round(TITLEBAR_H + PAD_TOP + len(CARD) * LINE_H + PAD_BOTTOM, 1)

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Terminal profile card for Aditya More: Data Scientist and Machine Learning Engineer">',
        f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" '
        f'fill="{theme["bg"]}" stroke="{theme["border"]}"/>',
        f'  <path d="M0.5 10.5a10 10 0 0 1 10-10h{width - 21}a10 10 0 0 1 10 10v{TITLEBAR_H - 10}H0.5z" '
        f'fill="{theme["chrome"]}"/>',
        f'  <line x1="0.5" y1="{TITLEBAR_H}" x2="{width - 0.5}" y2="{TITLEBAR_H}" stroke="{theme["border"]}"/>',
    ]
    for i, key in enumerate(("dot1", "dot2", "dot3")):
        out.append(f'  <circle cx="{20 + i * 18}" cy="{TITLEBAR_H / 2}" r="5" fill="{theme[key]}"/>')
    out.append(
        f'  <text x="{width / 2}" y="{TITLEBAR_H / 2 + 4}" text-anchor="middle" fill="{theme["muted"]}" '
        f'font-family="{FONT}" font-size="11.5">{escape(TITLE)}</text>'
    )

    y = TITLEBAR_H + PAD_TOP + FONT_SIZE
    for line in CARD:
        if line:
            spans = "".join(
                f'<tspan fill="{theme[role]}">{escape(text)}</tspan>' for text, role in line
            )
            out.append(
                f'  <text x="{PAD_X}" y="{round(y, 1)}" font-family="{FONT}" font-size="{FONT_SIZE}" '
                f'xml:space="preserve">{spans}</text>'
            )
        y += LINE_H
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    for name, theme in THEMES.items():
        with open(name, "w", encoding="utf-8") as fh:
            fh.write(render(theme))
        print(f"wrote {name}")
