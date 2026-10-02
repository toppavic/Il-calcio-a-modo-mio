"""Genera tre proposte di stile grafico (copertina + pagina esercitazione)."""
import pathlib

QUI = pathlib.Path(__file__).parent

TEMI = {
    "a-classico": dict(
        nome="Stile A · Classico",
        fonts='''@font-face { font-family: Oswald; src: url(../gli-imbattibili/font/oswald.woff2); font-weight: 200 700; }
  @font-face { font-family: Inter; src: url(../gli-imbattibili/font/inter.woff2); font-weight: 100 900; }''',
        head="Oswald", head_w=700, body="Inter", upper=True,
        page_bg="#ffffff", text="#1d2421", muted="#5d6b65", title="#0f3d2e", accent="#d4a017",
        cover_bg="#0f3d2e", cover_text="#ffffff", cover_title2="#d4a017", cover_sub="#dce8e2",
        box_bg="#ffffff", box_border="#dfe5e1", key_bg="#fbf6e6",
        pitch_a="#3f8f5a", pitch_b="#46995f", line="#ffffff",
        att="#c8372d", att_style="dot", deff="#2a5db0", def_style="dot", def_num="#ffffff",
        gk="#f2c230", move="#f2c230", pas="#ffffff", radius="2mm", tricolore=False,
    ),
    "b-lavagna": dict(
        nome="Stile B · Lavagna tattica",
        fonts='''@font-face { font-family: Bebas; src: url(font/bebasneue-400.woff2); }
  @font-face { font-family: Barlow; src: url(font/barlow-400.woff2); font-weight: 400; }
  @font-face { font-family: Barlow; src: url(font/barlow-600.woff2); font-weight: 600 700; }''',
        head="Bebas", head_w=400, body="Barlow", upper=True,
        page_bg="#1e2622", text="#e9eee9", muted="#a9b5ae", title="#ffffff", accent="#ffcf33",
        cover_bg="#161c19", cover_text="#ffffff", cover_title2="#ffcf33", cover_sub="#c9d3cd",
        box_bg="#252f2a", box_border="#34413a", key_bg="#2e3424",
        pitch_a="#2a3530", pitch_b="#2a3530", line="#e9eee9",
        att="#ff7b6b", att_style="x", deff="#e9eee9", def_style="ring", def_num="#e9eee9",
        gk="#ffcf33", move="#ffcf33", pas="#e9eee9", radius="1mm", tricolore=False,
    ),
    "c-moderno": dict(
        nome="Stile C · Moderno italiano",
        fonts='''@font-face { font-family: BarlowC; src: url(font/barlowcondensed-600.woff2); font-weight: 600; }
  @font-face { font-family: BarlowC; src: url(font/barlowcondensed-700.woff2); font-weight: 700; }
  @font-face { font-family: Barlow; src: url(font/barlow-400.woff2); font-weight: 400; }
  @font-face { font-family: Barlow; src: url(font/barlow-600.woff2); font-weight: 600 700; }''',
        head="BarlowC", head_w=700, body="Barlow", upper=False,
        page_bg="#ffffff", text="#16202e", muted="#5f6b7a", title="#0b3d91", accent="#0b3d91",
        cover_bg="#f4f6f9", cover_text="#0b3d91", cover_title2="#16202e", cover_sub="#4a5566",
        box_bg="#f4f6f9", box_border="#f4f6f9", key_bg="#eaf0fa",
        pitch_a="#e8efe9", pitch_b="#e1eae3", line="#9db4a5",
        att="#d7263d", att_style="dot", deff="#0b3d91", def_style="dot", def_num="#ffffff",
        gk="#f4b400", move="#0b3d91", pas="#16202e", radius="3mm", tricolore=True,
    ),
}


def schema(t):
    """Schema 'Scivolamenti' disegnato con i colori del tema."""
    L, M, P = t["line"], t["move"], t["pas"]

    def att(x, y):
        if t["att_style"] == "x":
            return (f'<g stroke="{t["att"]}" stroke-width="4" stroke-linecap="round">'
                    f'<line x1="{x-8}" y1="{y-8}" x2="{x+8}" y2="{y+8}"/><line x1="{x+8}" y1="{y-8}" x2="{x-8}" y2="{y+8}"/></g>')
        return f'<circle cx="{x}" cy="{y}" r="11" fill="{t["att"]}" stroke="#fff" stroke-width="2"/>'

    def dif(x, y, n):
        if t["def_style"] == "ring":
            c = f'<circle cx="{x}" cy="{y}" r="12" fill="{t["pitch_a"]}" stroke="{t["deff"]}" stroke-width="2.5"/>'
        else:
            c = f'<circle cx="{x}" cy="{y}" r="12" fill="{t["deff"]}" stroke="#fff" stroke-width="2"/>'
        return c + (f'<text x="{x}" y="{y+4.5}" font-family="{t["head"]}" font-weight="700" font-size="13" '
                    f'text-anchor="middle" fill="{t["def_num"]}">{n}</text>')

    def freccia(d, col, dash=False):
        da = ' stroke-dasharray="7 5"' if dash else ''
        mid = "fm" if col == M else "fp"
        return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{mid})"/>'

    gk = (f'<circle cx="250" cy="32" r="11" fill="{t["gk"]}" stroke="#1d2421" stroke-width="2"/>'
          if t["def_style"] != "ring" else
          f'<circle cx="250" cy="32" r="11" fill="{t["pitch_a"]}" stroke="{t["gk"]}" stroke-width="2.5"/>'
          f'<text x="250" y="36.5" font-family="{t["head"]}" font-size="13" text-anchor="middle" fill="{t["gk"]}">P</text>')
    return f'''<svg class="diagram" viewBox="0 0 500 380">
  <defs>
    <marker id="fm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{M}"/></marker>
    <marker id="fp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{P}"/></marker>
    <pattern id="str" width="60" height="400" patternUnits="userSpaceOnUse"><rect width="30" height="400" fill="{t["pitch_a"]}"/><rect x="30" width="30" height="400" fill="{t["pitch_b"]}"/></pattern>
  </defs>
  <rect width="500" height="380" fill="url(#str)"/>
  <g fill="none" stroke="{L}" stroke-width="2.5">
    <rect x="10" y="10" width="480" height="360"/><rect x="103" y="10" width="294" height="110"/>
    <rect x="186" y="10" width="128" height="38"/><path d="M205,120 A55,55 0 0 0 295,120"/>
  </g>
  <rect x="216" y="2" width="68" height="8" fill="{L}"/>
  {gk}
  {att(55,215)}{att(165,320)}{att(320,330)}{att(440,285)}
  <circle cx="74" cy="228" r="5" fill="#fff" stroke="#1d2421" stroke-width="1.5"/>
  {freccia("M430,285 L333,325", P, True)}{freccia("M308,330 L180,322", P, True)}{freccia("M155,312 L68,228", P, True)}
  {freccia("M120,140 L97,184", M)}{freccia("M245,150 L200,150", M)}{freccia("M325,150 L280,148", M)}{freccia("M405,150 L360,146", M)}
  {dif(92,195,2)}{dif(186,150,5)}{dif(266,148,6)}{dif(346,146,3)}
</svg>'''


def pagina(t):
    up = "uppercase" if t["upper"] else "none"
    tric = ('<div class="tric"><i style="background:#009246"></i><i style="background:#ffffff"></i>'
            '<i style="background:#ce2b37"></i></div>') if t["tricolore"] else ""
    return f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><title>{t["nome"]}</title>
<style>
  {t["fonts"]}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #9aa39e; display: flex; gap: 24px; padding: 24px; font-family: {t["body"]}, sans-serif; color: {t["text"]}; }}
  .page {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; background: {t["page_bg"]}; padding: 18mm; box-shadow: 0 6px 24px rgba(0,0,0,.25); font-size: 10.5pt; line-height: 1.5; }}
  .h {{ font-family: {t["head"]}, sans-serif; font-weight: {t["head_w"]}; text-transform: {up}; letter-spacing: .02em; }}
  .kicker {{ font-family: {t["head"]}, sans-serif; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; font-size: 10pt; color: {t["accent"]}; }}
  .cover {{ background: {t["cover_bg"]}; color: {t["cover_text"]}; padding: 0; }}
  .cover .inner {{ position: absolute; left: 20mm; right: 20mm; top: 40mm; }}
  .cover h1 {{ font-size: 70pt; line-height: .92; margin: 8mm 0 7mm; color: {t["cover_text"]}; }}
  .cover h1 span {{ display: block; color: {t["cover_title2"]}; }}
  .cover .sub {{ font-size: 15pt; color: {t["cover_sub"]}; max-width: 140mm; line-height: 1.4; }}
  .cover .sub b {{ color: {t["cover_text"]}; }}
  .cover .badge {{ position: absolute; left: 20mm; right: 20mm; bottom: 24mm; display: flex; gap: 5mm; }}
  .cover .badge > div {{ flex: 1; border-top: 3px solid {t["accent"] if not t["tricolore"] else t["title"]}; padding-top: 3mm; }}
  .cover .badge .n {{ font-size: 26pt; line-height: 1; color: {t["cover_title2"] if not t["tricolore"] else t["title"]}; }}
  .cover .badge .l {{ font-size: 8.5pt; letter-spacing: .1em; text-transform: uppercase; color: {t["cover_sub"]}; margin-top: 1.5mm; }}
  .cover .brand {{ color: {t["accent"]}; }}
  .tric {{ position: absolute; top: 0; left: 0; right: 0; height: 5mm; display: flex; }}
  .tric i {{ flex: 1; }}
  .lines {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
  h2 {{ font-size: 30pt; line-height: 1.05; color: {t["title"]}; }}
  .obj {{ color: {t["muted"]}; margin: 2mm 0 5mm; }}
  .obj b {{ color: {t["title"]}; }}
  .diagram {{ width: 150mm; display: block; margin: 0 auto; border-radius: {t["radius"]}; }}
  .three {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; margin-top: 6mm; }}
  .box {{ background: {t["box_bg"]}; border: 1px solid {t["box_border"]}; border-radius: {t["radius"]}; padding: 4mm 4.5mm; font-size: 9.6pt; }}
  .box h4 {{ font-family: {t["head"]}, sans-serif; font-weight: {t["head_w"]}; text-transform: {up}; color: {t["title"]}; font-size: 13pt; letter-spacing: .03em; margin-bottom: 2mm; }}
  .box p {{ margin-bottom: 2mm; }}
  ul {{ list-style: none; }}
  li {{ padding-left: 5mm; position: relative; margin-bottom: 1.3mm; }}
  li::before {{ content: ""; position: absolute; left: 0; top: 2mm; width: 2mm; height: 2mm; border-radius: 50%; background: {t["accent"]}; }}
  .key {{ background: {t["key_bg"]}; border-color: {t["key_bg"]}; }}
  .footer {{ position: absolute; left: 18mm; right: 18mm; bottom: 9mm; display: flex; justify-content: space-between; font-size: 8pt; color: {t["muted"]}; border-top: 1px solid {t["box_border"]}; padding-top: 2.5mm; }}
</style></head>
<body>
<section class="page cover">
  {tric}
  <svg class="lines" viewBox="0 0 210 297" preserveAspectRatio="none"><g fill="none" stroke="{t["cover_text"]}" stroke-opacity=".08" stroke-width=".6"><rect x="15" y="160" width="180" height="200"/><rect x="60" y="160" width="90" height="35"/><rect x="82" y="160" width="46" height="12"/></g></svg>
  <div class="inner">
    <div class="kicker brand">Il calcio a modo mio</div>
    <h1 class="h">Gli<span>Imbattibili</span></h1>
    <p class="sub"><b>La costruzione della linea difensiva.</b> La progressione della Juniores che ha vinto il campionato senza perdere una partita.</p>
  </div>
  <div class="badge">
    <div><div class="n h">0</div><div class="l">Sconfitte</div></div>
    <div><div class="n h">3</div><div class="l">Progressioni</div></div>
    <div><div class="n h">1°</div><div class="l">In campionato</div></div>
  </div>
</section>
<section class="page">
  <div class="kicker">Progressione 1 di 3</div>
  <h2 class="h">Scivolamenti</h2>
  <p class="obj"><b>Obiettivo:</b> la linea si muove insieme in base alla posizione della palla.</p>
  {schema(t)}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul><li>Linea a 4 (2-5-6-3) + portiere</li><li>Attaccanti che muovono la palla davanti alla linea</li><li>Metà campo con area di rigore</li></ul></div>
    <div class="box"><h4>Svolgimento</h4><p>Gli attaccanti muovono la palla. I difensori si spostano curando la <b>posizione del corpo</b> e la <b>distanza tra i compagni</b>.</p><p>Quando la palla arriva sull'esterno la linea si spacca e forma <b>due linee</b>.</p></div>
    <div class="box key"><h4>Punti chiave</h4><ul><li>Posizione del corpo</li><li>Distanza tra i compagni</li><li>Occhi sempre sulla palla</li><li><b>Dare sempre copertura al compagno che attacca la palla</b></li></ul></div>
  </div>
  <div class="footer"><span>GLI IMBATTIBILI</span><span>La costruzione della linea difensiva</span><span>3</span></div>
</section>
</body></html>'''


for chiave, tema in TEMI.items():
    (QUI / f"stile-{chiave}.html").write_text(pagina(tema))
    print(chiave)
