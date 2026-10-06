"""Genera le immagini dei post social (carosello) partendo dagli schemi degli allenamenti.

Crea post-4x5.html (Instagram e Facebook, 1080 × 1350) e post-9x16.html (TikTok, 1080 × 1920).
Le immagini PNG si ottengono con strumenti/render-post.js.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
GI = QUI.parent.parent / "prodotti" / "gli-imbattibili"
a2 = (GI / "allenamento-02.html").read_text()
defs = re.search(r'<svg width="0" height="0".*?</svg>', a2, re.S).group(0)
FONT = "../../prodotti/gli-imbattibili/font"
MAT = "../../materiale"


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def mezzo_campo(contenuto):
    return f'''<svg class="schema" viewBox="0 0 500 380">
      <rect width="500" height="380" fill="url(#strisce)"/>
      <g fill="none" stroke="#fff" stroke-width="2.5">
        <rect x="10" y="10" width="480" height="360"/>
        <rect x="103" y="10" width="294" height="110"/><rect x="186" y="10" width="128" height="38"/>
        <path d="M205,120 A55,55 0 0 0 295,120"/>
      </g>
      <rect x="216" y="2" width="68" height="8" fill="#fff"/>
      {g(250, 32, "pP")}
      {contenuto}
    </svg>'''


# ---------- Schemi (identici a quelli dei PDF)
schema_cross = mezzo_campo(
    freccia("M236,350 L72,346", tratteggio=True)
    + freccia("M62,334 L58,104", tratteggio=True)
    + freccia("M40,250 L40,62", True)
    + freccia("M62,44 Q170,6 262,62", tratteggio=True)
    + g(40, 46, "pA", 2) + g(60, 346, "pA", 1) + g(440, 92, "pA") + g(450, 330, "pA")
    + g(250, 350, "pJ", "M", "#1d2421")
    + '<use href="#palla" x="56" y="54"/>'
    + g(140, 60, "pB", 2) + g(200, 74, "pB", 5) + g(262, 88, "pB", 6) + g(324, 102, "pB", 3)
    + g(172, 108, "pB", 4) + g(232, 122, "pB", 8))

# 4-2-3-1 (attacca verso destra: il 2 e il 7 sul lato destro, cioè in basso). Il 10 è quello che si gira.
blu = (g(80, 65, "pB", "3") + g(75, 125, "pB", "6") + g(75, 180, "pB", "5") + g(80, 240, "pB", "2")
       + g(160, 105, "pB", "8") + g(160, 205, "pB", "4")
       + g(275, 60, "pB", "11") + g(275, 245, "pB", "7") + g(395, 150, "pB", "9"))
rossi = (g(425, 70, "pA") + g(420, 125, "pA") + g(420, 185, "pA") + g(425, 235, "pA")
         + g(345, 95, "pA") + g(340, 200, "pA")
         + g(215, 60, "pA") + g(230, 120, "pA") + g(215, 245, "pA") + g(125, 150, "pA"))
schema_partita = f'''<svg class="schema" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/><line x1="250" y1="20" x2="250" y2="280"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle">50 m</text>
    {g(30, 150, "pP", "P", "#1d2421")}{g(470, 150, "pP", "P", "#1d2421")}
    {rossi}{blu}
    {freccia("M87,178 L284,154", tratteggio=True)}
    <path d="M300,150 q14,-4 18,10 q2,10 -6,14" stroke="#f2c230" stroke-width="2.5" fill="none" marker-end="url(#freccia-oro)"/>
    {g(296, 150, "pB", "10")}{freccia("M316,149 L381,150", tratteggio=True)}
    <text x="300" y="128" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle" letter-spacing="1">SI GIRA</text>
    <use href="#palla" x="88" y="190"/>
  </svg>'''

schema_gioco = f'''<svg class="schema" viewBox="60 0 380 340">
    <rect x="60" width="380" height="340" fill="url(#strisce)"/>
    <rect x="110" y="30" width="280" height="280" fill="none" stroke="#fff" stroke-width="2.5"/>
    <text x="250" y="332" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    <text x="415" y="175" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    {freccia("M180,188 L240,117", tratteggio=True)}{freccia("M261,110 L361,214", tratteggio=True)}
    <use href="#palla" x="190" y="214"/>
    {g(250, 30, "pJ", 9, "#1d2421")}{g(250, 105, "pJ", 10, "#1d2421")}
    {g(140, 120, "pB", 11)}{g(185, 200, "pB", 4)}{g(370, 225, "pB", 2)}{g(235, 280, "pB", 5)}
    {g(360, 110, "pA", 7)}{g(235, 190, "pA", 8)}{g(140, 275, "pA", 3)}{g(305, 270, "pA", 6)}
  </svg>'''

# ---------- Contenuti dei post (regole e punti presi dai fogli dell'allenatore)
POST = [
    dict(
        n=1, foto="allenamento-04.jpg",
        gancio="Come difendevamo<span>sui cross</span>",
        schema=schema_cross,
        titolo2="La diagonale invertita",
        testo2="Il mister dà palla a <b>X1</b>, che la passa a <b>X2</b>. X2 arriva sul fondo e crossa. La linea si sistema per <b>respingere</b>.",
        titolo3="Chi va dove",
        punti=["Il <b>terzino lato palla</b> leggermente sotto la linea della palla",
               "<b>Centrali</b> e <b>terzino opposto</b> in leggera diagonale",
               "Il <b>centrocampista più vicino</b> a cerniera tra terzino e centrale",
               "<b>L'altro centrocampista</b> tra i due centrali"],
    ),
    dict(
        n=2, foto="allenamento-04-b.jpg",
        gancio="Preventiva<span>1</span>",
        schema=schema_partita,
        titolo2="Partita “lavoro preventivo”",
        testo2="10 contro 10 su 50 m. Chi riceve nella <b>metà campo offensiva</b> e riesce a girarsi e <b>servire un compagno</b> vale più di un gol. Chi difende deve stargli addosso <b>prima</b> che arrivi la palla.",
        titolo3="Le regole",
        punti=["<b>2 tempi da 15'</b>",
               "Massimo <b>3 tocchi</b>",
               "<b>Gol = 1 punto</b>",
               "Chi riceve nella <b>metà campo offensiva</b>, ha il tempo di girarsi e fa un passaggio <b>verticale o diagonale</b> a un compagno:&nbsp;<b>2&nbsp;punti</b>"],
    ),
    dict(
        n=3, foto="allenamento-03.jpg",
        gancio="15 passaggi<span>= 1 punto</span>",
        schema=schema_gioco,
        titolo2="Gioco di posizione",
        testo2="<b>4 contro 4 + 2 jolly</b> (il 9 e il 10) in un quadrato di <b>30 × 30 m</b>. <b>15 passaggi</b> consecutivi = <b>1 punto</b>.",
        titolo3="Per renderlo difficile",
        punti=["Si gioca a <b>2 tocchi</b>",
               "I jolly hanno <b>1 solo tocco</b>",
               "Con meno tocchi bisogna <b>smarcarsi prima</b> e più in fretta"],
    ),
]

FIRMA = "La Juniores che ha vinto il campionato <b>senza perdere una partita</b>"


def slides(p, tot=4):
    num = lambda i: f'<div class="num">{i}/{tot}</div>'
    marchio = '<div class="marchio"><b>GLI IMBATTIBILI</b><span>Il calcio a modo mio</span></div>'
    punti = "".join(f"<li>{x}</li>" for x in p["punti"])
    return f'''
<section class="slide cop">
  <img class="bgimg" src="{MAT}/precampionato/{p["foto"]}">
  <div class="veil"></div>
  <img class="logo" src="{MAT}/brand/logo-cerchio.png">
  <div class="txt">
    <div class="kick">Gli Imbattibili · dai quaderni del mister</div>
    <h1>{p["gancio"]}</h1>
    <p class="sub">{FIRMA}</p>
    <div class="scorri">Scorri →</div>
  </div>
</section>
<section class="slide int">
  {num(2)}
  <div class="kicker">Esercitazione</div>
  <h2>{p["titolo2"]}</h2>
  <div class="riq">{p["schema"]}</div>
  <p class="desc">{p["testo2"]}</p>
  {marchio}
</section>
<section class="slide int">
  {num(3)}
  <div class="kicker">{p["titolo2"]}</div>
  <h2>{p["titolo3"]}</h2>
  <ul class="punti">{punti}</ul>
  {marchio}
</section>
<section class="slide fine">
  <img class="logo2" src="{MAT}/brand/logo-cerchio.png">
  <h1>Gli<span>Imbattibili</span></h1>
  <p class="sub">{FIRMA}. Gli allenamenti del precampionato, scritti a mano dal mister e messi in pagina.</p>
  <div class="azioni"><div>Salva il post</div><div>Seguici per il prossimo</div></div>
</section>'''


def pagina(w, h):
    alto = h > 1500
    css = f'''
@font-face {{ font-family: Oswald; src: url({FONT}/oswald.woff2) format("woff2"); font-weight: 200 700; }}
@font-face {{ font-family: Inter; src: url({FONT}/inter.woff2) format("woff2"); font-weight: 100 900; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #888; font-family: Inter, sans-serif; }}
.slide {{ width: {w}px; height: {h}px; position: relative; overflow: hidden; margin: 0 0 20px; }}
h1, h2 {{ font-family: Oswald, sans-serif; font-weight: 700; text-transform: uppercase; }}
.cop, .fine {{ background: #0c120f; color: #fff; }}
.cop .bgimg {{ position: absolute; inset: -40px; width: calc(100% + 80px); height: calc(100% + 80px); object-fit: cover; transform: rotate(-4deg) scale(1.08); filter: grayscale(1) contrast(1.1); opacity: .55; }}
.cop .veil {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,18,15,.97) 0%, rgba(12,18,15,.9) 36%, rgba(12,18,15,.5) 52%, rgba(12,18,15,.85) 66%, rgba(12,18,15,.98) 80%); }}
.cop .logo {{ position: absolute; top: {200 if alto else 40}px; left: 50%; transform: translateX(-50%); width: {620 if alto else 520}px; -webkit-mask-image: linear-gradient(180deg, #000 80%, transparent 100%); }}
.cop .txt {{ position: absolute; left: 80px; right: 80px; {'top: 860px' if alto else 'bottom: 80px'}; }}
.kick {{ font-family: Oswald, sans-serif; font-weight: 500; letter-spacing: .22em; text-transform: uppercase; font-size: 28px; color: #84b94a; }}
.cop h1, .fine h1 {{ font-size: {150 if alto else 130}px; line-height: .92; margin: 20px 0 28px; }}
.cop h1 span, .fine h1 span {{ color: #84b94a; display: block; }}
.sub {{ font-size: 36px; line-height: 1.4; color: #dfe6e1; }}
.sub b {{ color: #fff; }}
.scorri {{ margin-top: 40px; font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .15em; font-size: 30px; color: #84b94a; }}
.int {{ background: #fff; padding: {'0 80px 260px' if alto else '90px 80px 0'}; color: #1d2421; {'display: flex; flex-direction: column; justify-content: center;' if alto else ''} }}
.int .num {{ position: absolute; top: {90 if alto else 40}px; right: 60px; font-family: Oswald, sans-serif; font-size: 28px; color: #9aa59f; }}
.kicker {{ font-family: Oswald, sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: .2em; font-size: 28px; color: #d4a017; }}
.int h2 {{ font-size: 78px; line-height: 1.02; color: #0f3d2e; margin: 10px 0 40px; }}
.riq {{ display: flex; justify-content: center; }}
.riq .schema {{ width: 100%; max-height: {900 if alto else 700}px; display: block; border-radius: 16px; }}
.desc {{ font-size: 36px; line-height: 1.45; margin-top: 40px; }}
.desc b, .punti b {{ color: #0f3d2e; }}
.punti {{ list-style: none; margin-top: 20px; }}
.punti li {{ font-size: 42px; line-height: 1.35; padding: 34px 0 34px 70px; position: relative; border-bottom: 2px solid #e3e8e5; }}
.punti li::before {{ content: ""; position: absolute; left: 0; top: 50px; width: 30px; height: 30px; background: #d4a017; border-radius: 50%; }}
.marchio {{ position: absolute; left: 80px; right: 80px; bottom: {150 if alto else 50}px; display: flex; justify-content: space-between; align-items: center; border-top: 3px solid #0f3d2e; padding-top: 22px; font-size: 26px; color: #5d6b65; }}
.marchio b {{ font-family: Oswald, sans-serif; color: #0f3d2e; letter-spacing: .12em; font-weight: 600; font-size: 30px; }}
.fine {{ display: flex; flex-direction: column; justify-content: center; padding: 0 80px; }}
.fine .logo2 {{ width: 340px; margin: 0 0 30px -20px; -webkit-mask-image: linear-gradient(180deg, #000 75%, transparent 100%); }}
.azioni {{ display: flex; gap: 24px; margin-top: 60px; }}
.azioni div {{ flex: 1; text-align: center; font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .08em; font-size: 32px; padding: 26px 10px; border-radius: 14px; background: #84b94a; color: #0c120f; }}
.azioni div + div {{ background: transparent; color: #fff; border: 2px solid #84b94a; }}
'''
    corpo = "".join(slides(p) for p in POST)
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Post social</title><style>{css}</style></head><body>{defs}{corpo}</body></html>'


(QUI / "post-4x5.html").write_text(pagina(1080, 1350))
(QUI / "post-9x16.html").write_text(pagina(1080, 1920))
print("ok")
