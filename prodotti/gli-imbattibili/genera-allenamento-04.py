"""Genera allenamento-04.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 4</title>")
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
             .replace("allenamento-01.jpg", "allenamento-04.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 4")
             .replace("la prima seduta della Juniores", "la quarta seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 4</span>'
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
      <div class="kicker">Precampionato · Settimana 1</div>
      <h2>Allenamento 4</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">95' + suicidi</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">50 m × largh.</div></div>
    <div><div class="l">Focus</div><div class="v">Marcature preventive</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “lavoro preventivo”</div><div class="d">Punti a chi riceve spalle alla porta e riesce a girarsi · vietato il compagno di reparto (gli attaccanti sì) · chi perde paga con i suicidi</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Lavoro a gruppi con cambio</div><div class="d">15' per gruppo · Gruppo A: cross in fase difensiva e 6 contro 4 con l'allenatore · Gruppo B: circuito di forza a 5 stazioni. Poi si invertono</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Parte atletica</div><div class="d">Intermittente a tempi decrescenti · 4 blocchi da 4' con 3' di recupero</div></td><td class="min">25'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Suicidi</div><div class="d">Per chi ha perso la partita iniziale</div></td><td class="min">–</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:30;background:var(--verde)">Lavoro a gruppi · 15' + 15'</div>
    <div style="flex:25;background:var(--oro);color:var(--verde)">Atletica · 25'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    In partita si premia chi riceve <b>spalle alla porta e si gira</b>: chi difende impara a marcare <b>prima</b> che l'avversario riceva. Nel lavoro a gruppi la linea difende sui cross e poi mette alla prova nel 6 contro 4 quello che ha imparato nei giorni precedenti.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita lavoro preventivo
def campo_partita():
    blu = (g(70, 70, "pB") + g(70, 130, "pB") + g(70, 190, "pB") + g(70, 245, "pB")
           + g(160, 60, "pB") + g(170, 150, "pB") + g(160, 240, "pB")
           + g(285, 85, "pB") + g(300, 205, "pB") + g(380, 140, "pB"))
    rossi = (g(430, 70, "pA") + g(430, 135, "pA") + g(430, 200, "pA") + g(420, 255, "pA")
             + g(340, 60, "pA") + g(345, 255, "pA") + g(225, 75, "pA")
             + g(205, 215, "pA") + g(120, 100, "pA") + g(120, 205, "pA"))
    giocata = (freccia("M82,190 L284,154", tratteggio=True)
               + '<path d="M300,150 q14,-4 18,10 q2,10 -6,14" stroke="#f2c230" stroke-width="2.5" fill="none" marker-end="url(#freccia-oro)"/>'
               + g(296, 150, "pB")
               + freccia("M320,160 L452,152", tratteggio=True)
               + '<text x="300" y="128" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle" letter-spacing="1">SI GIRA</text>')
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:118mm;margin:0 auto">
    <rect x="0" y="0" width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">50 m</text>
    {g(30, 150, "pP", "P", "#1d2421")}{g(470, 150, "pP", "P", "#1d2421")}
    {rossi}{blu}
    {giocata}
    <use href="#palla" x="88" y="200"/>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “lavoro preventivo”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti</span><span class="chip">10 contro 10 + 2 portieri</span><span class="chip">Campo 50 m × tutta la larghezza</span><span class="chip">Diviso in 2 metà</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> marcature preventive. Chi attacca è premiato quando riceve spalle alla porta e riesce a girarsi, quindi chi difende deve stare addosso all'avversario <b>prima</b> che arrivi la palla.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li>Vietato passare al compagno di reparto (<b>gli attaccanti sì</b>)</li>
        <li>Chi riceve <b>spalle alla porta e si gira</b>: <b>1 punto</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li>Vietato passare al compagno di reparto (<b>gli attaccanti sì</b>)</li>
        <li>Chi riceve spalle alla porta e riesce a fare <b>passaggio laterale e verticale</b> senza essere attaccato: <b>2 punti</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo lungo 50 m e largo quanto il campo regolamentare, diviso in due metà</li>
      <li>Due squadre da 10 giocatori</li>
      <li>Un portiere per ogni lato corto</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Le due squadre si contendono il pallone a tocchi limitati. Il punto non arriva dal gol ma dalla <b>giocata spalle alla porta</b> descritta nei riquadri sopra.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Chi difende accorcia mentre la palla viaggia</li>
      <li>Non lasciare girare l'avversario</li>
      <li>Chi riceve controlla già orientato</li>
    </ul></div>
  </div>

  <div class="chiave">
    <span class="kicker">La posta in gioco · suicidi a fine allenamento</span>
    Chi perde: <b>5 suicidi</b> · chi vince: <b>1 suicidio</b> · pareggio: <b>4 suicidi per tutti</b>.
  </div>
  {footer()}
</section>'''

# ---------- 4. Cross in fase difensiva
cross = pagina_esercizio(
    "Esercitazione III · Gruppo A · 1 di 2", "Difendere sui cross",
    "posizionarsi nel modo giusto in area per affrontare e respingere il cross.",
    mezzo_campo(
        freccia("M236,350 L72,346", tratteggio=True)
        + freccia("M52,334 L40,128", tratteggio=True)
        + freccia("M48,104 Q170,40 236,82", tratteggio=True)
        + g(40, 112, "pA", 2) + g(60, 346, "pA", 1) + g(440, 92, "pA") + g(450, 330, "pA")
        + g(250, 350, "pJ", "M", "#1d2421")
        + '<use href="#palla" x="40" y="128"/>'
        + g(150, 80, "pB", 2) + g(215, 66, "pB", 5) + g(290, 66, "pB", 6) + g(355, 80, "pB", 3)
        + g(215, 128, "pB", 4) + g(290, 128, "pB", 8)
        + '<text x="250" y="374" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">MISTER</text>'),
    "<li>Linea a 4 + portiere, con il 4 e l'8 davanti</li><li>Attaccanti: X1, X2 e due in attesa del cross</li><li>Metà campo con area di rigore</li>",
    "<p>Il mister dà la palla a <b>X1</b>, che la passa a <b>X2</b> sulla fascia. X2 <b>crossa</b>.</p>"
    "<p>I difensori devono <b>posizionarsi nel modo giusto</b> per affrontare e <b>respingere</b> la palla.</p>",
    "<li>Sistemarsi mentre la palla arriva al crossatore</li><li>Guardare insieme palla e avversario</li><li>Respingere lontano e verso l'esterno</li>",
    chips='<span class="chip">15 minuti per gruppo, poi cambio</span><span class="chip">Conduce l\'allenatore</span>')

# ---------- 5. 6 contro 4 di verifica
sei4 = pagina_esercizio(
    "Esercitazione III · Gruppo A · 2 di 2", "6 contro 4 di verifica",
    "vedere se tutto quello su cui abbiamo lavorato nei giorni precedenti è stato assimilato e, se necessario, correggere.",
    mezzo_campo(
        g(40, 150, "pA") + g(460, 150, "pA") + g(250, 175, "pA")
        + g(60, 320, "pA") + g(250, 330, "pA") + g(440, 320, "pA")
        + '<use href="#palla" x="265" y="338"/>'
        + g(140, 140, "pB", 2) + g(210, 140, "pB", 5) + g(290, 140, "pB", 6) + g(360, 140, "pB", 3)),
    "<li>Linea a 4 + portiere</li><li>6 attaccanti: uno davanti alla linea, due larghi, tre dietro</li><li>Metà campo con area di rigore</li>",
    "<p>Partita <b>6 contro 4</b> verso la porta difesa dalla linea.</p>"
    "<p>L'allenatore osserva se i movimenti provati negli allenamenti precedenti vengono fatti da soli e, <b>se serve, ferma e corregge</b>.</p>",
    "<li>Scivolare insieme seguendo la palla</li><li>Uscita e copertura come in “Ti lascio alle spalle”</li><li>Leggere il lancio prima che parta</li>")

# ---------- 6. Circuito di forza
stazioni = [
    ("Addominali", "", "2 × 15"),
    ("Balzi a piedi uniti", "partendo da mezzo squat", "4 × 3 serie"),
    ("Corsa calciata + scatto", "5 m di corsa calciata e 5 m di scatto", "6 rip."),
    ("Flessioni", "", "2 × 15"),
    ("Balzi a piedi uniti in avanti", "", "4 × 3 serie"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    + (f'<div class="d">{d}</div>' if d else "") + f'</div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

forza = f'''<section class="page">
  <div class="kicker">Esercitazione III · Gruppo B</div>
  <div class="ex-title"><h2>Circuito di forza</h2></div>
  <div class="ex-sub">
    <span class="chip">15 minuti, poi cambio</span><span class="chip">5 stazioni</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> forza generale ed esplosiva, alternando lavoro a corpo libero e balzi.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>5 stazioni in sequenza</li>
      <li>Il gruppo lavora mentre l'altro è con l'allenatore</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si completano le serie di una stazione e si passa alla successiva, dalla 1 alla 5.</p>
      <p>Nei balzi “4 × 3 serie” sono <b>3 serie da 4 balzi</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Nei balzi spingere forte e atterrare morbidi</li>
      <li>Schiena dritta nel mezzo squat</li>
      <li>Qualità del gesto prima della velocità</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 7. Parte atletica + suicidi
blocchi = [("45\"-15\"", "15\" di allungo sul lato lungo, 45\" di recupero sulla diagonale"),
           ("20\"-20\"", "20\" di corsa su 100 m, 20\" di recupero"),
           ("15\"-15\"", "15\" di corsa su 80 m, 15\" di recupero"),
           ("10\"-10\"", "10\" di navetta su 16 m, 10\" di recupero")]
recupero = '<tr class="rec"><td class="min">3\'</td><td class="rit">Recupero</td><td>3 minuti di recupero prima del blocco successivo</td></tr>'
righe = recupero.join(f'<tr><td class="min">4\'</td><td class="rit">{r}</td><td>{d}</td></tr>' for r, d in blocchi)

atletica = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Parte atletica</h2></div>
  <div class="ex-sub">
    <span class="chip">25 minuti</span><span class="chip">4 blocchi da 4 minuti</span><span class="chip">3 minuti di recupero tra i blocchi</span><span class="chip">Intermittente</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> resistenza alla velocità. Il lavoro si accorcia e il ritmo cresce da un blocco all'altro.</p>
  <table class="intervalli">{righe}</table>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo intero per gli allunghi</li>
      <li>Distanze segnate a 100, 80 e 16 m</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni blocco dura 4 minuti: si alterna il tratto di corsa al recupero, con i tempi indicati in tabella.</p>
      <p>Tra un blocco e l'altro <b>3 minuti di recupero</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Rispettare i tempi di partenza</li>
      <li>Nella navetta frenare e ripartire bassi</li>
      <li>Stessa intensità fino all'ultima ripetuta</li>
    </ul></div>
  </div>

  <div class="kicker" style="margin-top:7mm">Esercitazione V</div>
  <div class="ex-title"><h2 style="font-size:17pt">Suicidi</h2></div>
  <div class="two" style="margin-top:3mm">
    <div class="box"><h4>Chi li fa</h4>Chi ha perso la partita iniziale: 5 suicidi. Chi ha vinto: 1. In caso di pareggio 4 per tutti.</div>
    <div class="box"><h4>Il suicidio</h4>Navetta dal limite dell'area piccola al limite dell'area grande, come nell'Allenamento 3.</div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, partita, cross, sei4, forza, atletica]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-04.html").write_text(html)
print("pagine:", PAG[0])
