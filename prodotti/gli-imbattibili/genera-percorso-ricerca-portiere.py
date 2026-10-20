"""Genera percorso-ricerca-del-portiere.html: Percorso 1 · La ricerca del portiere (7 tappe).

Il percorso è un prodotto a sé, staccato da Gli Imbattibili (20/10): niente riferimenti agli allenamenti
o alla Juniores. Regole fisse per tutte le tappe: giocatori e campo dalla tabella, 2 tempi da 15',
jolly solo se dispari, punti sempre uguali (portiere 1, recupero alto e gol 2, lancio dalla metà difensiva 3).

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
                      "<title>Il calcio a modo mio – La ricerca del portiere</title>")
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
.scala { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-top: 2mm; }
.scala div { border-radius: 2mm; padding: 2.5mm 3mm; background: var(--verde); color: #fff; font-size: 9pt; line-height: 1.3; display: flex; gap: 2.5mm; align-items: center; }
.scala div b { font-family: Oswald, sans-serif; font-size: 20pt; color: var(--oro); line-height: 1; }
.scala div.off { background: #eef1ee; color: #9aa7a1; text-decoration: line-through; }
.scala div.off b { color: #c3ccc7; }
.vincoli { display: flex; gap: 2mm; flex-wrap: wrap; }
.vincoli span { background: #fbf6e6; border: 1px solid #ecd9a0; color: #7a5c0c; border-radius: 1.5mm; padding: 1.2mm 3mm; font-size: 9.5pt; font-weight: 600; }
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
    return (f'<div class="footer"><b>IL CALCIO A MODO MIO</b><span>{TITOLO_PIEDE}</span>'
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



PUNTI = [(1, "Portiere trovato"), (2, "Recupero nella metà offensiva e gol"), (3, "Lancio dalla metà difensiva al portiere")]


def scala(validi):
    return '<div class="scala">' + "".join(
        f'<div class="{"" if p in validi else "off"}"><b>{p}</b><span>{t}</span></div>' for p, t in PUNTI) + "</div>"


def pagina_tappa(n, titolo, tocchi, vincoli, cambia, obiettivo, schema, validi, chiave):
    vinc = "".join(f"<span>{v}</span>" for v in [f"Massimo {tocchi} tocchi"] + vincoli)
    return f'''<section class="page">
  <div class="kicker">Tappa {n} di 7</div>
  <div class="ex-title"><h2>{titolo}</h2></div>
  <div class="ex-sub"><span class="chip">2 tempi da 15'</span><span class="chip">Da 7 contro 7 a 11 contro 11</span><span class="chip">Campo secondo la tabella</span></div>
  <div class="cambia"><b class="k">Cosa cambia</b><span>{cambia}</span></div>
  <p class="obj"><b>Obiettivo:</b> {obiettivo}</p>
  {schema}
  <h3 style="margin-top:5mm">Regole</h3>
  <div class="vincoli">{vinc}</div>
  <h3 style="margin-top:4mm">Punti</h3>
  {scala(validi)}
  <div class="box" style="margin-top:5mm"><h4>Punti chiave</h4><ul class="clean">{chiave}</ul></div>
  {footer()}
</section>'''


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
    <div class="kick">Il calcio a modo mio · Percorso 1</div>
    <h1>La ricerca<span>del portiere</span></h1>
    <p class="sub"><b>7 tappe in progressione, dalla più facile alla più difficile,</b> per costruire una squadra che pressa alto, legge la palla, verticalizza con qualità e fa circolare la palla in modo funzionale.</p>
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
    <p>La <b>ricerca del portiere</b> è una partita a tema: per fare punto bisogna far arrivare la palla al <b>portiere avversario</b>, che fa da bersaglio dentro la sua porta. Ogni passaggio deve avere uno scopo: avvicinare la palla al bersaglio.</p>
    <p>Il pressing è questione di corsa e <b>si impara a correre insieme, come squadra</b>. Tappa dopo tappa cambiano solo le regole e con le regole cambiano i comportamenti: chi attacca impara a smarcarsi, a verticalizzare e a pressare alto; chi difende impara a leggere la palla e a restare corto e compatto.</p>
  </div>
  <h3 style="margin-top:4mm">Obiettivi</h3>
  <div class="obiettivi">
    <div class="box"><h4>Con la palla</h4><ul class="clean">
      <li><b>Circolazione di palla funzionale</b>: ogni passaggio serve ad avanzare verso il bersaglio.</li>
      <li><b>Verticalizzazione rapida e di qualità</b>: pochi tocchi, passaggi in avanti, smarcamenti tra le linee.</li>
    </ul></div>
    <div class="box"><h4>Senza palla</h4><ul class="clean">
      <li><b>Pressione alta</b>: persa palla si aggredisce subito.</li>
      <li><b>Palla coperta e palla scoperta</b>: con palla scoperta la linea difensiva scappa e toglie profondità, con palla coperta accorcia in avanti.</li>
      <li><b>Linea compatta</b>: reparti corti per togliere le filtranti.</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ======================================================================
# 3. REGOLE FISSE
def pallino(colore, bordo="#fff"):
    return f'<svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="{colore}" stroke="{bordo}" stroke-width="2"/></svg>'


freccia_oro = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg>'
passaggio = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg>'

base = f'''<section class="page">
  <div class="kicker">Prima di cominciare</div>
  <div class="ex-title"><h2>Le regole fisse</h2></div>
  <p class="obj">Valgono in tutte e 7 le tappe. Le tappe cambiano solo i tocchi, i vincoli e quali punti valgono.</p>
  <div class="regole">
    <div class="box"><h4>Il bersaglio</h4>Ogni squadra attacca verso il portiere avversario. Il punto vale solo se il portiere riceve la palla <b>stando dentro la porta</b>.</div>
    <div class="box"><h4>I punti</h4>Sono sempre gli stessi. In ogni tappa trovi quali valgono.{scala([1, 2, 3])}</div>
    <div class="box"><h4>Durata e jolly</h4><b>2 tempi da 15'</b>. Con un numero dispari di giocatori si aggiunge un <b>jolly sempre con la squadra in possesso</b>.</div>
  </div>
  <h3 style="margin-top:6mm">Giocatori e campo</h3>
  <table class="campi">
    <tr><td>7 c 7 · 8 c 8</td><td>50 m di lunghezza × 40 m di larghezza</td></tr>
    <tr><td>9 c 9</td><td>Metà campo regolamentare (circa 50-55 × 65 m)</td></tr>
    <tr><td>10 c 10</td><td>Circa 60 m di lunghezza × tutta la larghezza del campo</td></tr>
    <tr><td>11 c 11</td><td>Tre quarti di campo (circa 70-75 × 65 m)</td></tr>
  </table>
  <h3 style="margin-top:6mm">Come leggere gli schemi</h3>
  <div class="legenda">
    <div>{pallino("#c8372d")} Rossi: attaccano verso destra</div>
    <div>{pallino("#2a5db0")} Blu: attaccano verso sinistra</div>
    <div>{pallino("#f2c230", "#1d2421")} Portiere bersaglio</div>
    <div>{freccia_oro} Movimento o pressione</div>
    <div>{passaggio} Passaggio o lancio</div>
  </div>
  {footer()}
</section>'''

# ======================================================================
# 4. MAPPA
MAPPA = [
    ("Trovare il portiere", "3 tocchi", "1"),
    ("Leggere la profondità", "3 tocchi", "1 · 3"),
    ("Solo verticale", "3 tocchi · solo verticale", "1 · 3"),
    ("Cambiare reparto", "2 tocchi · no compagno di reparto", "1 · 2 · 3"),
    ("Pressione senza lancio", "2 tocchi · no lancio", "1 · 2"),
    ("Pressione e verticalità", "2 tocchi · no lancio · solo verticale", "1 · 2"),
    ("La partita completa", "3 tocchi · tutto libero", "1 · 2 · 3"),
]
righe = "".join(
    f'<tr><td class="n">{i}</td><td class="t">{t}</td><td>{v}</td><td style="font-family:Oswald;color:var(--oro);font-size:12pt">{p}</td></tr>'
    for i, (t, v, p) in enumerate(MAPPA, 1))
salita = "".join(f'<div style="height:{30 + i * 10}%">{i + 1}</div>' for i in range(7))

mappa = f'''<section class="page">
  <div class="kicker">La progressione</div>
  <div class="ex-title"><h2>Le 7 tappe dal facile al difficile</h2></div>
  <div class="salita">{salita}</div>
  <table class="mappa">
    <tr><th></th><th>Tappa</th><th>Regole</th><th>Punti validi</th></tr>
    {righe}
  </table>
  {footer()}
</section>'''

# ======================================================================
# 5-11. LE TAPPE
base_passaggi = (freccia("M150,146 L200,100", tratteggio=True) + freccia("M210,96 L295,84", tratteggio=True)
                 + freccia("M305,84 L372,144", tratteggio=True) + freccia("M388,150 L455,150", tratteggio=True)
                 + '<use href="#palla" x="160" y="160"/>')
lancio = (freccia("M85,214 Q270,40 455,146", tratteggio=True) + '<use href="#palla" x="96" y="230"/>'
          + etichetta(255, 42, "LANCIO DALLA METÀ DIFENSIVA · 3", "#f2c230", 11))
pressione = (freccia("M300,210 L340,165", oro=True) + freccia("M380,164 L358,158", oro=True)
             + freccia("M300,90 L338,138", oro=True)
             + freccia("M356,150 L455,150", tratteggio=True) + etichetta(330, 262, "RECUPERO ALTO E GOL · 2", "#f2c230", 11))

t1 = pagina_tappa(1, "Trovare il portiere", 3, [],
    "È il punto di partenza: si impara il gioco e il suo bersaglio.",
    "smarcarsi, giocare a testa alta e far arrivare la palla al portiere.",
    campo(base_passaggi + etichetta(430, 135, "1", "#f2c230", 14)), [1],
    "<li>Smarcarsi sempre per offrire una linea di passaggio</li><li>Guardare il portiere prima di ricevere</li>")

t2 = pagina_tappa(2, "Leggere la profondità", 3, [],
    "Vale anche il lancio dalla metà difensiva, 3 punti.",
    "riconoscere la palla scoperta: chi attacca lancia, la linea che difende scappa e toglie profondità.",
    campo(lancio + freccia("M415,92 L440,70", oro=True) + freccia("M415,208 L440,230", oro=True)
          + etichetta(395, 265, "LA LINEA SCAPPA", "#ffffff", 10)), [1, 3],
    "<li>Lanciare solo con palla scoperta</li><li>Con palla scoperta la linea scappa</li><li>Chi è vicino al portatore lo pressa per coprire la palla</li>")

t3 = pagina_tappa(3, "Solo verticale", 3, ["Solo verticale: mai passaggi orizzontali"],
    "Sparisce il passaggio orizzontale.",
    "verticalizzare: passaggi in avanti, all'indietro o in diagonale.",
    campo(freccia("M214,108 L214,192", tratteggio=True) + no(214, 168)
          + freccia("M92,84 L142,140", tratteggio=True) + freccia("M158,148 L292,86", tratteggio=True)
          + freccia("M306,84 L372,146", tratteggio=True) + '<use href="#palla" x="97" y="96"/>'), [1, 3],
    "<li>Smarcarsi in diagonale, mai in linea con il portatore</li><li>Lo scarico all'indietro prepara la verticalizzazione</li>")

t4 = pagina_tappa(4, "Cambiare reparto", 2, ["Vietato passare al compagno di reparto (gli attaccanti a chi vogliono)"],
    "Si scende a 2 tocchi, niente passaggi al compagno di reparto e vale anche il recupero alto con gol.",
    "giocare tra le linee coinvolgendo tutti i reparti e cominciare a pressare alto.",
    campo(freccia("M85,214 L85,92", tratteggio=True) + no(85, 150)
          + freccia("M92,214 L198,104", tratteggio=True) + '<use href="#palla" x="97" y="230"/>' + pressione), [1, 2, 3],
    "<li>Cercare il compagno della linea davanti o dietro</li><li>Persa palla, aggredire subito</li>")

t5 = pagina_tappa(5, "Pressione senza lancio", 2, ["No lancio"],
    "Il lancio è vietato: al portiere si arriva solo palla a terra.",
    "pressione alta. Senza lancio la palla è spesso coperta: la squadra accorcia in avanti e la linea sale.",
    campo(pressione), [1, 2],
    "<li>Si pressa tutti insieme, correndo come squadra</li><li>Con palla coperta la linea accorcia in avanti</li><li>Dopo il recupero attaccare subito la porta</li>")

t6 = pagina_tappa(6, "Pressione e verticalità", 2, ["No lancio", "Solo verticale"],
    "Alla pressione senza lancio si aggiunge il gioco solo verticale.",
    "pressare alto e, dopo il recupero, verticalizzare subito senza passaggi orizzontali.",
    campo(pressione + freccia("M150,146 L200,100", tratteggio=True) + freccia("M210,96 L295,84", tratteggio=True)
          + '<use href="#palla" x="160" y="160"/>'), [1, 2],
    "<li>Recupero e prima giocata in avanti</li><li>Reparti corti per togliere le filtranti</li>")

t7 = pagina_tappa(7, "La partita completa", 3, ["Tutte le soluzioni sono libere"],
    "Torna il lancio e valgono tutti i punti: la squadra sceglie ogni volta la soluzione migliore.",
    "mettere insieme tutto il percorso: costruire, lanciare con palla scoperta, pressare per riconquistare in alto.",
    campo(lancio + pressione), [1, 2, 3],
    "<li>Palla scoperta: lancio per chi attacca, linea che scappa per chi difende</li><li>Palla coperta: costruire corto, linea che accorcia</li><li>Persa palla, pressione immediata</li>")

# ======================================================================
# 12. CHIUSURA
chiusura = f'''<section class="page">
  <div class="kicker">Il calcio a modo mio</div>
  <div class="ex-title"><h2>Gli altri percorsi</h2></div>
  <div class="chiave" style="margin-top:6mm">
    <span class="kicker">Il calcio a modo mio</span>
    Gli altri percorsi sono nel negozio Etsy <b>ilcalcioamodomio</b>. Gli esercizi della settimana sono su Instagram <b>@ilcalcio.amodomio</b>.
  </div>
  {footer()}
</section>'''

pagine = [copertina, presentazione, base, mappa, t1, t2, t3, t4, t5, t6, t7]
html = testa + "\n\n".join(pagine) + "\n\n</body>\n</html>\n"
(QUI / "percorso-ricerca-del-portiere.html").write_text(html)
print("pagine:", len(pagine))
