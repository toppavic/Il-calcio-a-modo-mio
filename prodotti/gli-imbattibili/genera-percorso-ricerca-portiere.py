"""Genera percorso-ricerca-del-portiere.html: Percorso 1 · La ricerca del portiere (7 tappe).

Contenuti decisi con l'allenatore il 17/10 (vedi prodotti/percorsi/ricerca-del-portiere/bozza.md):
progressione sempre dal facile al difficile, scrittura e grafica professionali.
Uso: python3 genera-percorso-ricerca-portiere.py  poi  render.js sul file .html
"""
import pathlib

QUI = pathlib.Path(__file__).parent
a2 = (QUI / "allenamento-02.html").read_text()
TITOLO_PIEDE = "Percorso 1 · La ricerca del portiere"

testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – La ricerca del portiere</title>")
testa = testa.replace("</style>\n</head>", """
.cop { background: #0d1c2e; color: #fff; padding: 0 !important; }
.cop .campo { position: absolute; left: 15mm; top: 84mm; width: 180mm; opacity: .9; }
.cop .logo { position: absolute; top: 12mm; left: 50%; transform: translateX(-50%); width: 92mm; }
.cop .txt { position: absolute; left: 20mm; right: 20mm; bottom: 22mm; }
.cop .kick { font-family: Oswald, sans-serif; font-weight: 500; letter-spacing: .25em; text-transform: uppercase; font-size: 10.5pt; color: #d4a017; }
.cop h1 { font-family: Oswald, sans-serif; font-weight: 700; text-transform: uppercase; line-height: .95; font-size: 50pt; margin: 3mm 0 4mm; }
.cop h1 span { color: #d4a017; display: block; }
.cop .sub { font-size: 13pt; color: #d6deea; line-height: 1.45; max-width: 165mm; }
.cop .sub b { color: #fff; }
.cop .marchio { position: absolute; top: 108mm; left: 20mm; font-family: Oswald, sans-serif; letter-spacing: .3em; font-size: 9pt; color: #84b94a; text-transform: uppercase; }
.domande { margin: 6mm 0 6mm; }
.domande p { font-family: Oswald, sans-serif; font-size: 17pt; color: var(--verde); line-height: 1.3; margin-bottom: 2mm; }
.domande p::before { content: "›"; color: var(--oro); margin-right: 3mm; }
.testo p { font-size: 10.8pt; line-height: 1.6; margin-bottom: 3mm; }
.obiettivi { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-top: 4mm; }
.obiettivi .box h4 { color: var(--oro); }
.obiettivi li { margin-bottom: 2mm; }
.mappa { width: 100%; border-collapse: collapse; margin-top: 4mm; }
.mappa th { font-family: Oswald, sans-serif; text-transform: uppercase; font-weight: 500; font-size: 8.5pt; letter-spacing: .08em; color: var(--tenue); text-align: left; padding: 0 2mm 2mm; border-bottom: 2px solid var(--verde); }
.mappa td { padding: 3mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 9.4pt; vertical-align: top; }
.mappa .n { font-family: Oswald, sans-serif; font-size: 20pt; color: var(--oro); width: 10mm; line-height: 1; }
.mappa .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 11.5pt; }
.mappa .f { color: var(--tenue); font-size: 8.5pt; }
.salita { display: flex; align-items: flex-end; gap: 2mm; height: 26mm; margin: 2mm 0 1mm; }
.salita div { flex: 1; background: var(--verde); border-radius: 1mm 1mm 0 0; color: var(--oro); font-family: Oswald, sans-serif; font-size: 12pt; display: flex; align-items: flex-start; justify-content: center; padding-top: 1mm; }
.cambia { display: flex; gap: 3mm; align-items: flex-start; background: #fbf6e6; border-left: 4px solid var(--oro); border-radius: 0 2mm 2mm 0; padding: 2.5mm 4mm; margin: 0 0 3.5mm; font-size: 9.6pt; }
.cambia b.k { font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .1em; color: #9a7410; font-weight: 500; white-space: nowrap; font-size: 8.5pt; padding-top: .4mm; }
.regole { display: grid; gap: 3mm; margin-top: 4mm; }
.regole .box { background: var(--fondo); border: 0; }
.regole .box h4 { margin-bottom: 1mm; }
.punti { display: flex; gap: 2mm; flex-wrap: wrap; margin-top: 1.5mm; }
.punti span { background: var(--verde); color: #fff; border-radius: 1.5mm; padding: 1mm 2.5mm; font-size: 8.8pt; }
.punti span b { color: var(--oro); font-family: Oswald, sans-serif; font-size: 10.5pt; margin-right: 1mm; }
.fonte { position: absolute; left: 18mm; right: 18mm; bottom: 16mm; font-size: 8pt; color: var(--tenue); font-style: italic; }
.campi { width: 100%; border-collapse: collapse; margin-top: 2mm; }
.campi td { padding: 2.6mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10pt; }
.campi td:first-child { font-family: Oswald, sans-serif; color: var(--verde); font-size: 12pt; width: 34mm; }
.legenda { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 6mm; margin-top: 3mm; font-size: 10pt; }
.legenda div { display: flex; align-items: center; gap: 3mm; }
</style>
</head>""", 1)

PAG = [0]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>{TITOLO_PIEDE}</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def etichetta(x, y, testo, col="#fff", size=11, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="Oswald" font-size="{size}" font-weight="700" fill="{col}" '
            f'text-anchor="{anchor}" letter-spacing="1">{testo}</text>')


def no(x, y):
    """Croce rossa su un passaggio vietato."""
    return (f'<g stroke="#ff4d3d" stroke-width="4" stroke-linecap="round">'
            f'<line x1="{x-8}" y1="{y-8}" x2="{x+8}" y2="{y+8}"/><line x1="{x+8}" y1="{y-8}" x2="{x-8}" y2="{y+8}"/></g>')


# Squadra rossa attacca verso destra (portiere a destra), blu verso sinistra
ROSSI = [(85, 80), (85, 220), (150, 150), (205, 95), (205, 205), (300, 80), (300, 220), (380, 150)]
BLU = [(415, 85), (415, 215), (350, 150), (290, 120), (290, 185), (195, 150), (120, 105), (120, 195)]


def campo(contenuto, rossi=ROSSI, blu=BLU, larghezza="150mm", jolly=None):
    gioc = "".join(g(x, y, "pA") for x, y in rossi) + "".join(g(x, y, "pB") for x, y in blu)
    if jolly:
        gioc += g(jolly[0], jolly[1], "pJ", "J", "#1d2421")
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:{larghezza};margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="20" width="420" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/><circle cx="250" cy="150" r="30"/>
    </g>
    <g fill="none" stroke="#fff" stroke-width="3"><rect x="22" y="122" width="18" height="56"/><rect x="460" y="122" width="18" height="56"/></g>
    {g(31, 150, "pP")}{g(469, 150, "pP")}
    {etichetta(145, 294, "METÀ DIFENSIVA DEI ROSSI", "#ffffff", 10)}{etichetta(355, 294, "METÀ OFFENSIVA DEI ROSSI", "#ffffff", 10)}
    {gioc}
    {contenuto}
  </svg>'''


def pagina_tappa(n, titolo, fonte, chips, cambia, obiettivo, schema, regole_html, org, svol, chiave):
    chips_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
    return f'''<section class="page">
  <div class="kicker">Tappa {n} di 7</div>
  <div class="ex-title"><h2>{titolo}</h2></div>
  <div class="ex-sub">{chips_html}</div>
  <div class="cambia"><b class="k">Cosa cambia</b><span>{cambia}</span></div>
  <p class="obj"><b>Obiettivo:</b> {obiettivo}</p>
  {schema}
  <div class="regole">{regole_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">{org}</ul></div>
    <div class="box"><h4>Svolgimento</h4>{svol}</div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">{chiave}</ul></div>
  </div>
  <div class="fonte">Dagli Imbattibili: {fonte}</div>
  {footer()}
</section>'''


def regola(titolo, righe, punti=()):
    pts = "".join(f'<span><b>{p}</b>{t}</span>' for p, t in punti)
    pts_html = f'<div class="punti">{pts}</div>' if punti else ""
    li = "".join(f"<li>{r}</li>" for r in righe)
    return f'<div class="box"><h4>{titolo}</h4><ul class="clean">{li}</ul>{pts_html}</div>'


def due_regole(a, b):
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm">{a}{b}</div>'


# ======================================================================
# 1. COPERTINA
campo_cop = f'''<svg class="campo" viewBox="0 0 500 300">
  <g fill="none" stroke="#2c4b6e" stroke-width="2"><rect x="20" y="20" width="460" height="260"/>
  <line x1="250" y1="20" x2="250" y2="280"/><circle cx="250" cy="150" r="34"/>
  <rect x="4" y="118" width="16" height="64"/><rect x="480" y="118" width="16" height="64"/></g>
  <circle cx="488" cy="150" r="10" fill="#f2c230"/>
  <g fill="#c8372d" stroke="#fff" stroke-width="1.5"><circle cx="90" cy="90" r="8"/><circle cx="150" cy="190" r="8"/><circle cx="235" cy="120" r="8"/><circle cx="330" cy="200" r="8"/><circle cx="395" cy="110" r="8"/></g>
  <g fill="#2a5db0" stroke="#fff" stroke-width="1.5"><circle cx="190" cy="80" r="8"/><circle cx="280" cy="160" r="8"/><circle cx="360" cy="150" r="8"/><circle cx="420" cy="215" r="8"/></g>
  <g fill="none" stroke-width="3" stroke-dasharray="8 6"><path d="M90,90 Q160,40 235,120" stroke="#ffffff"/><path d="M235,120 Q320,60 395,110" stroke="#ffffff"/><path d="M395,110 Q450,120 480,148" stroke="#d4a017"/></g>
</svg>'''

copertina = f'''<section class="page cop">
  <img class="logo" src="../../materiale/brand/logo-cerchio.png">
  {campo_cop}
  <div class="txt">
    <div class="kick">Gli Imbattibili · Percorso 1</div>
    <h1>La ricerca<span>del portiere</span></h1>
    <p class="sub"><b>7 tappe in progressione</b> per costruire una squadra che pressa alto, verticalizza con qualità e fa circolare la palla in modo funzionale. Dai quaderni dell'allenatore della Juniores che ha vinto il campionato senza perdere una partita.</p>
  </div>
</section>'''

# ======================================================================
# 2. PRESENTAZIONE
presentazione = f'''<section class="page">
  <div class="kicker">Il percorso</div>
  <div class="ex-title"><h2>A chi serve questo percorso</h2></div>
  <div class="domande">
    <p>Vuoi costruire una squadra che pressi alto?</p>
    <p>Che sappia leggere palla coperta e palla scoperta?</p>
    <p>Che impari a verticalizzare velocemente e con qualità?</p>
    <p>Che faccia circolare la palla in modo funzionale, non fine a se stesso?</p>
  </div>
  <div class="testo">
    <p>La <b>ricerca del portiere</b> è la partita a tema con cui la Juniores che ha vinto il campionato provinciale senza perdere una partita ha costruito il suo modo di stare in campo, dal primo giorno di precampionato fino al campionato.</p>
    <p>Il principio è semplice: per fare punto bisogna far arrivare la palla al <b>portiere avversario</b>, che fa da bersaglio dentro la sua porta. Ogni passaggio deve avere uno scopo: avvicinare la palla al bersaglio.</p>
    <p>Tappa dopo tappa cambiano solo le regole (tocchi, vincoli e punteggi) e con le regole cambiano i comportamenti. Chi attacca impara a smarcarsi, a verticalizzare e a pressare alto. Chi difende impara a leggere la palla: scappare quando è scoperta, accorciare quando è coperta, restare corto e compatto per togliere le filtranti.</p>
  </div>
  <h3 style="margin-top:4mm">Obiettivi</h3>
  <div class="obiettivi">
    <div class="box"><h4>Con la palla</h4><ul class="clean">
      <li><b>Circolazione di palla funzionale</b>: ogni passaggio serve ad avanzare verso il bersaglio, non a tenere palla.</li>
      <li><b>Verticalizzazione rapida e di qualità</b>: pochi tocchi, passaggi in avanti, smarcamenti tra le linee.</li>
    </ul></div>
    <div class="box"><h4>Senza palla</h4><ul class="clean">
      <li><b>Pressione alta</b>: chi perde palla aggredisce subito e il recupero vicino alla porta avversaria vale di più.</li>
      <li><b>Palla coperta e palla scoperta</b>: con palla scoperta la linea difensiva scappa e toglie profondità, con palla coperta accorcia in avanti.</li>
      <li><b>Linea compatta</b>: reparti corti e vicini per togliere le filtranti.</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ======================================================================
# 3. REGOLE DI BASE, CAMPI, LEGENDA
def pallino(colore, bordo="#fff"):
    return f'<svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="{colore}" stroke="{bordo}" stroke-width="2"/></svg>'


freccia_oro = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg>'
passaggio = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg>'

base = f'''<section class="page">
  <div class="kicker">Prima di cominciare</div>
  <div class="ex-title"><h2>Le regole di base</h2></div>
  <div class="regole" style="margin-top:4mm">
    <div class="box"><h4>Il bersaglio</h4>Ogni squadra attacca verso il portiere avversario. Il punto è valido solo quando il portiere riceve la palla <b>stando dentro la porta</b>: così il passaggio deve essere preciso e pulito.</div>
    <div class="box"><h4>Il jolly</h4>Se i giocatori sono in numero dispari si gioca con un <b>jolly che sta sempre con la squadra in possesso</b>. Con la palla si impara a sfruttare la superiorità numerica, senza palla a gestire l'inferiorità.</div>
    <div class="box"><h4>La progressione</h4>Le tappe vanno <b>dalla più facile alla più difficile</b>. Ognuna aggiunge una regola alla precedente: si passa alla tappa successiva quando la squadra ha fatto suoi i comportamenti di quella prima.</div>
  </div>

  <h3 style="margin-top:7mm">Il campo in base ai giocatori</h3>
  <table class="campi">
    <tr><td>7 c 7 · 8 c 8</td><td>50 m di lunghezza × 40 m di larghezza</td></tr>
    <tr><td>9 c 9</td><td>Metà campo regolamentare (circa 50-55 × 65 m)</td></tr>
    <tr><td>10 c 10</td><td>Circa 60 m di lunghezza × tutta la larghezza del campo</td></tr>
    <tr><td>11 c 11</td><td>Tre quarti di campo (circa 70-75 × 65 m)</td></tr>
  </table>
  <p class="obj" style="margin-top:2mm;font-size:9pt">In ogni tappa trovi il numero di giocatori con cui è stata fatta. Per giocare con un numero diverso usa questa tabella.</p>

  <h3 style="margin-top:6mm">Come leggere gli schemi</h3>
  <div class="legenda">
    <div>{pallino("#c8372d")} Squadra rossa: attacca verso destra</div>
    <div>{pallino("#2a5db0")} Squadra blu: attacca verso sinistra</div>
    <div>{pallino("#f2c230", "#1d2421")} Portiere bersaglio, dentro la porta</div>
    <div>{pallino("#ffffff", "#1d2421")} Jolly con chi ha la palla</div>
    <div>{freccia_oro} Movimento o pressione</div>
    <div>{passaggio} Passaggio o lancio</div>
  </div>
  {footer()}
</section>'''

# ======================================================================
# 4. MAPPA DELLA PROGRESSIONE
MAPPA = [
    ("Trovare il portiere", "3 tocchi", "Portiere trovato: 1 punto", "Smarcarsi, testa alta, circolazione funzionale"),
    ("Leggere la profondità", "2 tocchi", "Il lancio dalla metà difensiva vale 2 punti", "Palla scoperta: lanciare o scappare"),
    ("Solo verticale", "3 tocchi · solo verticale", "Niente passaggi orizzontali", "Verticalizzare"),
    ("Cambiare reparto e recuperare alto", "2 tocchi · no compagno di reparto", "Conta anche il recupero nella metà offensiva", "Giocare tra le linee, prima pressione"),
    ("Pressione senza lancio", "3 tocchi · no lancio", "Recupero alto e gol: 3 punti", "Pressione alta, palla coperta"),
    ("Costruire e pressare", "2 tocchi · no lancio", "1, 2 o 3 punti", "Costruzione da dietro e riconquista alta"),
    ("La partita completa", "3 tocchi · da 7c7 a 11c11", "1, 2 o 3 punti con il lancio", "Tutto insieme, a squadre intere"),
]
righe = "".join(
    f'<tr><td class="n">{i}</td><td><div class="t">{t}</div><div class="f">{v}</div></td><td>{c}</td><td>{f}</td></tr>'
    for i, (t, v, c, f) in enumerate(MAPPA, 1))
salita = "".join(f'<div style="height:{30 + i * 10}%">{i + 1}</div>' for i in range(7))

mappa = f'''<section class="page">
  <div class="kicker">La progressione</div>
  <div class="ex-title"><h2>Le 7 tappe dal facile al difficile</h2></div>
  <div class="salita">{salita}</div>
  <p class="obj" style="font-size:9pt">Ogni tappa aggiunge una sola regola: tocchi, vincoli o punteggi. La difficoltà cresce un passo alla volta.</p>
  <table class="mappa">
    <tr><th></th><th>Tappa e vincoli</th><th>Cosa si aggiunge</th><th>Cosa allena</th></tr>
    {righe}
  </table>
  {footer()}
</section>'''

# ======================================================================
# 5-11. LE TAPPE
CHIP_10 = ["10 contro 10 + 2 portieri", "Campo 50 m × tutta la larghezza"]

t1 = pagina_tappa(
    1, "Trovare il portiere", "Allenamento 1, primo tempo",
    ["15 minuti"] + CHIP_10 + ["3 tocchi"],
    "È il punto di partenza: si impara il gioco e il suo bersaglio.",
    "circolazione di palla funzionale. Smarcarsi, giocare a testa alta e far arrivare la palla al portiere avversario.",
    campo(freccia("M150,146 L200,100", tratteggio=True) + freccia("M210,96 L295,84", tratteggio=True)
          + freccia("M305,84 L372,144", tratteggio=True) + freccia("M388,150 L455,150", tratteggio=True)
          + '<use href="#palla" x="160" y="160"/>' + etichetta(430, 135, "1 PUNTO", "#f2c230", 12)),
    regola("Regole", ["Massimo <b>3 tocchi</b>"], [("1", "punto ogni volta che il portiere riceve la palla")]),
    "<li>Campo diviso in due metà</li><li>Due squadre, un portiere bersaglio per lato</li>",
    "<p>Le squadre si contendono la palla. Chi è in possesso deve farla arrivare al portiere del lato che attacca.</p>",
    "<li>Smarcarsi sempre per offrire una linea di passaggio</li><li>Guardare il portiere prima di ricevere</li><li>Chi difende resta corto</li>")

t2 = pagina_tappa(
    2, "Leggere la profondità", "Allenamento 1, secondo tempo (e Allenamento 2, primo tempo)",
    ["15 minuti"] + CHIP_10 + ["2 tocchi"],
    "I tocchi scendono a 2 e il lancio dalla metà difensiva vale doppio.",
    "riconoscere la palla scoperta. Chi attacca capisce quando c'è il tempo per il lancio; la linea che difende capisce quando deve scappare.",
    campo(freccia("M85,214 Q270,40 455,146", tratteggio=True) + '<use href="#palla" x="96" y="230"/>'
          + etichetta(255, 42, "LANCIO · 2 PUNTI", "#f2c230", 12)
          + freccia("M415,92 L440,70", oro=True) + freccia("M415,208 L440,230", oro=True)
          + freccia("M350,140 L395,118", oro=True)
          + etichetta(395, 265, "LA LINEA SCAPPA", "#ffffff", 10)),
    regola("Regole", ["Massimo <b>2 tocchi</b>"],
           [("1", "portiere trovato dalla metà offensiva"), ("2", "portiere trovato con un lancio dalla metà difensiva")]),
    "<li>Come la tappa 1</li><li>Metà difensiva e metà offensiva ben segnate</li>",
    "<p>Si gioca a 2 tocchi. Il lancio dalla propria metà campo è premiato: chi difende deve leggere quando il portatore è libero.</p>",
    "<li>Lanciare solo con palla scoperta</li><li>Con palla scoperta la linea scappa e toglie profondità</li><li>Chi è vicino al portatore lo pressa per coprire la palla</li>")

t3 = pagina_tappa(
    3, "Solo verticale", "Allenamento 2, secondo tempo",
    ["15 minuti"] + CHIP_10 + ["3 tocchi", "Solo verticale"],
    "Sparisce il passaggio orizzontale: si gioca solo in avanti, all'indietro o in diagonale.",
    "verticalizzare. La squadra deve cercare sempre la linea davanti e smarcarsi in diagonale rispetto alla palla.",
    campo(freccia("M85,86 L198,96", tratteggio=True) + no(140, 90)
          + freccia("M92,84 L142,140", tratteggio=True) + freccia("M158,148 L292,86", tratteggio=True)
          + freccia("M306,84 L372,146", tratteggio=True) + '<use href="#palla" x="97" y="96"/>'),
    regola("Regole", ["Massimo <b>3 tocchi</b>", "<b>Solo gioco verticale</b>: passaggi in avanti, all'indietro o in diagonale, mai orizzontali"],
           [("1", "portiere trovato dalla metà offensiva"), ("2", "portiere trovato con un lancio dalla metà difensiva")]),
    "<li>Come le tappe precedenti</li>",
    "<p>Stesso punteggio della tappa 2. Il passaggio orizzontale è vietato: se c'è, la palla passa agli avversari.</p>",
    "<li>Smarcarsi in diagonale, mai in linea con il portatore</li><li>Lo scarico all'indietro prepara la verticalizzazione</li><li>Chi difende chiude le linee centrali</li>")

t4 = pagina_tappa(
    4, "Cambiare reparto e recuperare alto", "Allenamento 5, primo tempo",
    ["15 minuti"] + CHIP_10 + ["2 tocchi", "No compagno di reparto"],
    "Vietato passare al compagno del proprio reparto. Per la prima volta conta anche il recupero nella metà offensiva.",
    "giocare tra le linee coinvolgendo tutti i reparti e dare la prima spinta alla pressione alta.",
    campo(freccia("M85,214 L85,92", tratteggio=True) + no(85, 150)
          + freccia("M92,214 L198,104", tratteggio=True) + '<use href="#palla" x="97" y="230"/>'
          + freccia("M300,210 L340,165", oro=True) + freccia("M380,164 L355,160", oro=True)
          + etichetta(330, 255, "RECUPERO ALTO", "#f2c230", 11)),
    regola("Regole", ["Massimo <b>2 tocchi</b>", "Vietato passare al <b>compagno di reparto</b> (gli attaccanti possono passarla a chi vogliono)"],
           [("2", "portiere trovato con un lancio dalla metà difensiva"), ("1", "portiere trovato dopo un recupero nella metà offensiva")]),
    "<li>Come le tappe precedenti</li><li>Reparti chiari: difesa, centrocampo, attacco</li>",
    "<p>Il punto vale solo se il portiere viene trovato con un lancio dalla metà difensiva o dopo un recupero nella metà offensiva.</p>",
    "<li>Cercare il compagno della linea davanti o dietro</li><li>Persa palla, aggredire subito</li><li>La linea difensiva legge la palla e scappa se è scoperta</li>")

ROSSI7 = [(110, 95), (110, 205), (190, 150), (280, 90), (280, 210), (345, 150), (400, 110)]
BLU7 = [(425, 175), (390, 220), (320, 115), (240, 150), (200, 80), (170, 220), (95, 150)]

t5 = pagina_tappa(
    5, "Pressione senza lancio", "Allenamento 16",
    ["30 minuti · 2 tempi da 15'", "7 contro 7 + jolly", "Campo 50 × 40 m", "3 tocchi", "No lancio"],
    "Il lancio è vietato: al portiere si arriva solo palla a terra. Il recupero nella metà offensiva diventa il premio più grande.",
    "pressione alta. Senza lancio la palla è spesso coperta: la squadra senza palla può accorciare in avanti e la linea difensiva salire.",
    campo(freccia("M345,162 L378,206", oro=True) + freccia("M400,122 L392,198", oro=True)
          + freccia("M280,198 L372,212", oro=True) + '<use href="#palla" x="398" y="226"/>'
          + freccia("M370,214 L455,160", tratteggio=True) + etichetta(300, 262, "RECUPERO ALTO E GOL · 3 PUNTI", "#f2c230", 11),
          rossi=ROSSI7, blu=BLU7, jolly=(250, 60), larghezza="136mm"),
    due_regole(regola("1° tempo · 15'", ["Massimo <b>3 tocchi</b>", "<b>No lancio</b>"],
                      [("1", "portiere trovato"), ("3", "gol dopo un recupero nella metà offensiva")]),
               regola("2° tempo · 15'", ["Stesse regole", "In più <b>solo gioco verticale</b>"])),
    "<li>Due squadre da 7 e un jolly con chi ha palla</li><li>Un portiere per lato</li>",
    "<p>Dopo un recupero nella metà offensiva si può tirare in porta: il gol vale 3 punti. Nel 2° tempo si aggiunge il gioco verticale.</p>",
    "<li>Pressione immediata quando si perde palla</li><li>Dopo il recupero attaccare subito la porta</li><li>Con palla coperta la linea accorcia in avanti</li>")

t6 = pagina_tappa(
    6, "Costruire e pressare", "Allenamento 17",
    ["30 minuti · 2 tempi da 15'", "7 contro 7", "Metà campo larga quanto l'area", "2 tocchi", "No lancio"],
    "Tre modi diversi di fare punto: il punteggio premia sia la costruzione da dietro sia la riconquista alta.",
    "costruire da dietro e pressare alto nella stessa partita. Chi trova il portiere partendo dalla metà difensiva vale il doppio.",
    campo(freccia("M110,103 L182,146", tratteggio=True) + freccia("M196,146 L272,94", tratteggio=True)
          + freccia("M288,90 L455,146", tratteggio=True) + '<use href="#palla" x="122" y="112"/>'
          + etichetta(360, 42, "DA DIETRO · 2 PUNTI", "#f2c230", 11)
          + freccia("M345,162 L385,212", oro=True) + etichetta(330, 262, "RECUPERO ALTO E GOL · 3 PUNTI", "#f2c230", 11),
          rossi=ROSSI7, blu=BLU7, larghezza="122mm"),
    due_regole(regola("1° tempo · 15'", ["Massimo <b>2 tocchi</b> · <b>no lancio</b>"],
                      [("1", "passaggio al portiere"), ("2", "passaggio al portiere partendo dalla metà difensiva"),
                       ("3", "recupero nella metà offensiva: si deve cercare il gol")]),
               regola("2° tempo · 15'", ["Stesse regole", "In più vietato passare al <b>compagno di reparto</b> (gli attaccanti con chi vogliono)"])),
    "<li>Metà campo larga quanto l'area di rigore, divisa in due</li><li>Un portiere bersaglio per lato</li>",
    "<p>Dopo un recupero nella metà offensiva non si cerca il portiere ma il gol.</p>",
    "<li>Costruire da dietro per i 2 punti</li><li>Pressione alta per i 3 punti</li><li>Reparti corti per togliere le filtranti</li>")

t7 = pagina_tappa(
    7, "La partita completa", "regole decise dall'allenatore per chiudere il percorso",
    ["2 tempi da 15'", "Da 7 contro 7 a 11 contro 11", "Campo secondo la tabella", "3 tocchi", "Jolly se dispari"],
    "Torna il lancio e si gioca fino a squadre intere: la squadra sceglie ogni volta la soluzione migliore.",
    "mettere insieme tutto il percorso. Costruire, lanciare quando la palla è scoperta, pressare per riconquistare in alto. La linea difensiva legge la palla e toglie le filtranti.",
    campo(freccia("M85,214 Q270,30 455,146", tratteggio=True) + '<use href="#palla" x="96" y="230"/>'
          + etichetta(255, 40, "LANCIO DALLA METÀ DIFENSIVA · 3 PUNTI", "#f2c230", 11)
          + freccia("M300,210 L340,165", oro=True) + freccia("M380,164 L355,160", oro=True)
          + freccia("M352,152 L455,152", tratteggio=True)
          + etichetta(340, 262, "RECUPERO ALTO E GOL · 2 PUNTI", "#f2c230", 11), larghezza="126mm"),
    regola("Regole", ["Massimo <b>3 tocchi</b>", "Campo in base al numero di giocatori (vedi la tabella delle regole di base)",
                      "Con un numero dispari, <b>jolly</b> sempre con chi ha la palla"],
           [("1", "portiere trovato"), ("3", "portiere trovato con un lancio dalla metà difensiva"),
            ("2", "gol dopo un recupero nella metà offensiva")]),
    "<li>Da 7c7 fino a 11c11</li><li>Un portiere bersaglio per lato</li>",
    "<p>Tutte le soluzioni sono valide: la squadra deve capire quale scegliere in base alla situazione della palla.</p>",
    "<li>Palla scoperta: lancio per chi attacca, linea che scappa per chi difende</li><li>Palla coperta: costruire corto, linea che accorcia</li><li>Persa palla, pressione immediata</li>")

# ======================================================================
# 12. CHIUSURA
chiusura = f'''<section class="page">
  <div class="kicker">Gli Imbattibili</div>
  <div class="ex-title"><h2>Da dove viene questo percorso</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Le tappe di questo percorso sono tratte dagli allenamenti veri della <b>Juniores provinciale che ha vinto il campionato senza perdere una partita</b>, con soli 8 gol subiti in tutta la stagione. Sono state riordinate dall'allenatore in progressione, dalla più facile alla più difficile, e completate con l'ultima tappa che riassume tutto il lavoro.</p>
    <p>Gli allenamenti completi della stagione, seduta per seduta, sono raccolti nei pacchetti della serie <b>Gli Imbattibili</b>:</p>
  </div>
  <div class="regole">
    <div class="box"><h4>Il precampionato · Allenamenti 1-10</h4>Le prime dieci sedute, dal primo giorno di preparazione.</div>
    <div class="box"><h4>In campionato · Allenamenti 11-19</h4>Le prime quattro settimane di campionato, con le partite del fine settimana.</div>
    <div class="box"><h4>Il libro · Gli Imbattibili</h4>La storia della stagione, su Amazon. Il libro racconta cosa è successo, gli allenamenti mostrano come ci siamo arrivati.</div>
  </div>
  <div class="chiave" style="margin-top:8mm">
    <span class="kicker">Il calcio a modo mio</span>
    Trovi tutti i pacchetti nel negozio Etsy <b>ilcalcioamodomio</b> e gli esercizi della settimana su Instagram <b>@ilcalcio.amodomio</b>.
  </div>
  {footer()}
</section>'''

pagine = [copertina, presentazione, base, mappa, t1, t2, t3, t4, t5, t6, t7, chiusura]
html = testa + "\n\n".join(pagine) + "\n\n</body>\n</html>\n"
(QUI / "percorso-ricerca-del-portiere.html").write_text(html)
print("pagine:", len(pagine))
