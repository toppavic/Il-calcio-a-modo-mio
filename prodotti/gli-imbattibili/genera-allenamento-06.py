"""Genera allenamento-06.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 6</title>")
testa = testa.replace("</style>\n</head>", """.stazioni { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; margin: 2mm 0 5mm; }
.stazione { display: flex; gap: 4mm; align-items: center; background: #f3f5f2; border-radius: 2mm; padding: 3.5mm 4mm; }
.stazione .n { flex: none; width: 10mm; height: 10mm; border-radius: 50%; background: var(--verde); color: var(--oro); font-family: Oswald, sans-serif; font-weight: 700; font-size: 15pt; display: flex; align-items: center; justify-content: center; }
.stazione .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 12pt; letter-spacing: .02em; line-height: 1.2; }
.stazione .d { font-size: 9.5pt; color: #5d6b65; margin-top: .5mm; }
.stazione .q { margin-left: auto; flex: none; font-family: Oswald, sans-serif; font-size: 13pt; color: var(--verde); font-weight: 700; text-align: right; }
.intervalli { width: 100%; border-collapse: collapse; margin: 1mm 0 5mm; }
.intervalli td { padding: 3mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10pt; vertical-align: middle; }
.intervalli .min { font-family: Oswald, sans-serif; font-size: 15pt; color: var(--verde); width: 14mm; }
.intervalli tr.rec td { background: #f3f5f2; color: #5d6b65; padding: 1.5mm 2mm; }
.intervalli tr.rec .min, .intervalli tr.rec .rit { font-size: 11pt; color: #7aa995; }
.intervalli .rit { font-family: Oswald, sans-serif; font-size: 13pt; color: #9a7410; width: 26mm; }
</style>
</head>""", 1)
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("allenamento-01.jpg", "allenamento-06.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 6")
             .replace("la prima seduta della Juniores", "la sesta seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 6</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def mezzo_campo(contenuto, larghezza="150mm"):
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:{larghezza};margin:0 auto">
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


def pagina_esercizio(kicker, titolo, obiettivo, schema, org, svol, chiave, chips=""):
    chips_html = f'<div class="ex-sub">{chips}</div>' if chips else ""
    return f'''<section class="page">
  <div class="kicker">{kicker}</div>
  <div class="ex-title"><h2>{titolo}</h2></div>
  {chips_html}
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> {obiettivo}</p>
  {schema}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">{org}</ul></div>
    <div class="box"><h4>Svolgimento</h4>{svol}</div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">{chiave}</ul></div>
  </div>
  {footer()}
</section>'''


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">Precampionato · Settimana 2</div>
      <h2>Allenamento 6</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">100'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">50 m × largh.</div></div>
    <div><div class="l">Focus</div><div class="v">Pressione e squadra corta</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Pressione nella metà offensiva</div><div class="d">Partita a squadra corta · il gol vale solo se tutta la squadra è nella metà offensiva · 2 tempi da 15'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Stazioni di forza</div><div class="d">Circuito a 5 stazioni per tutto il gruppo</div></td><td class="min">25'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Attacco contro difesa</div><div class="d">9 contro 9 a tocco libero · 2 tempi da 10-12'</div></td><td class="min">25'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita libera</div><div class="d">Senza vincoli</div></td><td class="min">10'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Pressione · 30'</div>
    <div style="flex:25;background:var(--oro);color:var(--verde)">Forza · 25'</div>
    <div style="flex:25;background:var(--verde)">Attacco-difesa · 25'</div>
    <div style="flex:10;background:#7aa995">10'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Si lavora sulla <b>squadra corta</b>: in partita il gol conta solo se tutti sono saliti nella metà offensiva e il recupero palla in avanti vale triplo. Poi, nell'attacco contro difesa, si curano i movimenti difensivi senza fermare il gioco.
  </div>
  {footer()}
</section>'''

# ---------- 3. Pressione nella metà offensiva
def campo_pressione():
    blu = (g(270, 70, "pB") + g(275, 145, "pB") + g(270, 225, "pB")
           + g(320, 50, "pB") + g(330, 115, "pB") + g(325, 185, "pB") + g(320, 250, "pB")
           + g(375, 90, "pB") + g(395, 150, "pB") + g(375, 210, "pB"))
    rossi = (g(440, 75, "pA") + g(445, 130, "pA") + g(440, 190, "pA") + g(435, 245, "pA")
             + g(355, 150, "pA") + g(300, 85, "pA") + g(300, 205, "pA")
             + g(130, 90, "pA") + g(150, 170, "pA") + g(120, 240, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:118mm;margin:0 auto">
    <rect x="0" y="0" width="500" height="300" fill="url(#strisce)"/>
    <rect x="252" y="21" width="217" height="258" fill="#f2c230" opacity=".13"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
      <rect x="16" y="125" width="14" height="50"/><rect x="470" y="125" width="14" height="50"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">50 m</text>
    <text x="360" y="294" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" letter-spacing="1">METÀ OFFENSIVA BLU · TUTTI DENTRO</text>
    {g(42, 150, "pP")}{g(458, 150, "pP")}
    {rossi}{blu}
    {freccia("M384,146 L366,150", True)}
    <use href="#palla" x="356" y="162"/>
  </svg>'''

pressione = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Pressione nella metà offensiva</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Campo 50 m × tutta la larghezza</span><span class="chip">Squadra corta</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> pressare in avanti con la squadra corta. Per segnare tutta la squadra deve salire nella metà offensiva e il recupero palla alto è premiato.</p>
  {campo_pressione()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li><b>Solo gioco verticale</b>: passaggi in avanti, all'indietro o in diagonale, mai orizzontali</li>
        <li>Gol dopo un <b>recupero nella metà offensiva</b>: <b>3 punti</b></li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Vietato passare al compagno di reparto</li>
        <li>Gol dopo un <b>recupero nella metà offensiva</b>: <b>3 punti</b></li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo lungo 50 m e largo quanto il campo regolamentare, diviso in due metà</li>
      <li>Due squadre da 10 giocatori</li>
      <li>Due porte con i portieri</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita con porte. Chi attacca deve accompagnare l'azione con tutta la squadra: se un giocatore è rimasto nella metà difensiva il gol non vale.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Salire tutti insieme, anche i difensori</li>
      <li>Persa palla, aggredire subito</li>
      <li>Squadra corta: poca distanza tra i reparti</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Stazioni di forza
stazioni = [
    ("Addominali", "", "3 × 10"),
    ("Balzi a piedi uniti con rimbalzo", "partendo dalla posizione di mezzo squat", "3 × 5"),
    ("Skip + scatto", "5 m di skip e 5 m di scatto", "8 rip."),
    ("Flessioni", "", "3 × 10"),
    ("Balzi in avanti su un piede", "", "3 × 8 colpi"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    + (f'<div class="d">{d}</div>' if d else "") + f'</div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

forza = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Stazioni di forza</h2></div>
  <div class="ex-sub">
    <span class="chip">25 minuti</span><span class="chip">5 stazioni</span><span class="chip">Tutto il gruppo</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> forza generale ed esplosiva. Rispetto all'Allenamento 4 crescono le serie e arrivano i balzi su un piede.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>5 stazioni in sequenza</li>
      <li>Tutto il gruppo lavora insieme</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si completano le serie di una stazione e si passa alla successiva, dalla 1 alla 5.</p>
      <p>Nei balzi su un piede “3 × 8 colpi” sono <b>3 serie da 8 balzi</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Nel rimbalzo restare reattivi, poco tempo a terra</li>
      <li>Schiena dritta nel mezzo squat</li>
      <li>Qualità del gesto prima della velocità</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. Attacco contro difesa + partita libera
attacco_svg = mezzo_campo(
    g(110, 150, "pB", 2) + g(200, 145, "pB", 5) + g(300, 145, "pB", 6) + g(390, 150, "pB", 3)
    + g(150, 220, "pB") + g(250, 212, "pB") + g(350, 222, "pB") + g(200, 295, "pB") + g(305, 295, "pB")
    + g(60, 200, "pA") + g(205, 185, "pA") + g(300, 190, "pA") + g(440, 195, "pA")
    + g(105, 260, "pA") + g(250, 262, "pA") + g(400, 262, "pA") + g(170, 345, "pA") + g(330, 345, "pA")
    + '<use href="#palla" x="182" y="352"/>', "122mm")

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Attacco contro difesa</h2></div>
  <div class="ex-sub">
    <span class="chip">25 minuti · 2 tempi da 10-12'</span><span class="chip">9 contro 9 + portiere</span><span class="chip">Tocco libero</span><span class="chip">Conduce l'allenatore</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rivedere in situazione di gioco i movimenti difensivi provati nei giorni precedenti.</p>
  {attacco_svg}
  <div class="two">
    <div class="box"><h4>1° obiettivo</h4>Lavoro sulla cura dei <b>movimenti difensivi</b>.</div>
    <div class="box"><h4>Obiettivo secondario</h4>Lavoro sui <b>movimenti offensivi</b>, <b>senza fermare il gioco</b>.</div>
  </div>

  <div class="kicker" style="margin-top:7mm">Esercitazione V</div>
  <div class="ex-title"><h2 style="font-size:17pt">Partita libera · 10'</h2></div>
  <div class="box" style="margin-top:3mm">Partita a fine seduta senza vincoli di tocchi o di punteggio.</div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, pressione, forza, attacco]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-06.html").write_text(html)
print("pagine:", PAG[0])
