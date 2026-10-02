"""Genera allenamento-05.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 5</title>")
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
             .replace("allenamento-01.jpg", "allenamento-05.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 5")
             .replace("la prima seduta della Juniores", "la quinta seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 5</span>'
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
      <h2>Allenamento 5</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">113'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">50 m × largh.</div></div>
    <div><div class="l">Focus</div><div class="v">Uscite e coperture</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “ricerca del portiere”</div><div class="d">2 tocchi · lancio dalla metà difensiva e recupero palla nella metà offensiva premiati · nel 2° tempo solo gioco verticale</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Lavoro a gruppi con cambio</div><div class="d">20' per gruppo · Gruppo A: fase difensiva, uscite della difesa contro il centrocampo · Gruppo B: rondo, 4 serie da 3'. Poi si invertono</div></td><td class="min">40'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Parte atletica · navette</div><div class="d">Intermittente a tempi decrescenti · 4 blocchi da 6' con 3' di recupero</div></td><td class="min">33'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:40;background:var(--verde)">Lavoro a gruppi · 20' + 20'</div>
    <div style="flex:33;background:var(--oro);color:var(--verde)">Atletica · 33'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il tema è l'<b>uscita</b>: in partita il recupero palla nella metà offensiva vale un punto, mentre nel lavoro a gruppi la difesa impara a uscire sul centrocampo restando coperta alle spalle con le <b>piramidi</b>.
  </div>
  {footer()}
</section>'''

# ---------- 3. Ricerca del portiere
def campo_partita():
    blu = (g(70, 70, "pB") + g(70, 130, "pB") + g(70, 190, "pB") + g(70, 245, "pB")
           + g(160, 60, "pB") + g(170, 150, "pB") + g(160, 240, "pB")
           + g(285, 85, "pB") + g(300, 205, "pB") + g(380, 140, "pB"))
    rossi = (g(430, 70, "pA") + g(430, 135, "pA") + g(430, 200, "pA") + g(420, 255, "pA")
             + g(340, 60, "pA") + g(345, 255, "pA") + g(225, 75, "pA")
             + g(205, 215, "pA") + g(120, 100, "pA") + g(120, 205, "pA"))
    lancio = (freccia("M82,190 Q260,110 452,148", tratteggio=True)
              + '<text x="250" y="122" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle" letter-spacing="2">LANCIO · 2 PUNTI</text>')
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:118mm;margin:0 auto">
    <rect x="0" y="0" width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">50 m</text>
    <text x="140" y="294" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">METÀ DIFENSIVA BLU</text>
    <text x="360" y="294" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">METÀ OFFENSIVA BLU</text>
    {g(30, 150, "pP", "P", "#1d2421")}{g(470, 150, "pP", "P", "#1d2421")}
    {rossi}{blu}
    {lancio}
    <use href="#palla" x="88" y="200"/>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “ricerca del portiere”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti</span><span class="chip">10 contro 10 + 2 portieri</span><span class="chip">Campo 50 m × tutta la larghezza</span><span class="chip">Diviso in 2 metà</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> cercare la profondità con il lancio e recuperare palla in avanti. Si gioca a 2 tocchi per tutta la partita.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Vietato passare al compagno di reparto (<b>gli attaccanti sì</b>)</li>
        <li>Portiere trovato con un <b>lancio dalla metà difensiva</b>: <b>2 punti</b></li>
        <li>Portiere trovato dopo un <b>recupero nella metà offensiva</b>: <b>1 punto</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li><b>Solo gioco verticale</b>: passaggi in avanti, all'indietro o in diagonale, mai orizzontali</li>
        <li>Portiere trovato dopo un <b>lancio</b>: <b>2 punti</b></li>
        <li>Portiere trovato dopo un <b>recupero nella metà offensiva</b>: <b>1 punto</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo lungo 50 m e largo quanto il campo regolamentare, diviso in due metà</li>
      <li>Due squadre da 10 giocatori</li>
      <li>Un portiere per ogni lato corto, che fa da bersaglio</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra deve far arrivare la palla al portiere del lato che attacca. Il punto vale solo se arriva con un lancio o dopo un recupero in avanti.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Testa alta: guardare la profondità prima di ricevere</li>
      <li>Appena persa palla, aggredire subito</li>
      <li>Con 2 tocchi il controllo deve già preparare il passaggio</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Fase difensiva: uscite difesa contro centrocampo
def campo_uscite():
    return f'''<svg class="diagram" viewBox="0 0 500 330" style="width:128mm;margin:0 auto">
    <rect width="500" height="330" fill="url(#strisce)"/>
    <rect x="60" y="45" width="380" height="240" fill="none" stroke="#fff" stroke-width="2.5"/>
    {g(250, 22, "pJ", "A", "#1d2421")}{g(250, 308, "pJ", "C", "#1d2421")}
    {freccia("M110,112 L110,192", True)}
    {freccia("M205,106 L170,140", True)}{freccia("M295,100 L270,130", True)}
    {g(110, 100, "pB", 2)}{g(215, 95, "pB", 5)}{g(305, 90, "pB", 6)}{g(390, 100, "pB", 3)}
    <g opacity=".45">{g(110, 205, "pB", 2)}{g(160, 150, "pB", 5)}{g(262, 140, "pB", 6)}</g>
    {g(110, 240, "pA")}{g(205, 250, "pA")}{g(295, 250, "pA")}{g(390, 240, "pA")}
    <use href="#palla" x="122" y="250"/>
    <text x="72" y="160" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" letter-spacing="1" transform="rotate(-90 72 160)">USCITA</text>
  </svg>'''

uscite = f'''<section class="page">
  <div class="kicker">Esercitazione III · Gruppo A</div>
  <div class="ex-title"><h2>Uscite della difesa sul centrocampo</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti per gruppo, poi cambio</span><span class="chip">2 parti da 10'</span><span class="chip">Conduce l'allenatore</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> uscire sul centrocampista in possesso senza lasciare spazio alle spalle, curando le piramidi e le coperture d'uscita.</p>
  {campo_uscite()}
  <div class="two">
    <div class="box">
      <h4>1ª parte · 10'</h4>
      <p>Uscite della <b>difesa contro il centrocampo</b>. È importante curare le <b>piramidi</b> e le <b>coperture d'uscita</b>.</p>
    </div>
    <div class="box">
      <h4>2ª parte · 10'</h4>
      <p>Si gioca a punti: <b>1 punto</b> ogni volta che i centrocampisti trovano <b>A</b> oppure i difensori trovano <b>C</b>.</p>
    </div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>4 difensori (D) e 4 centrocampisti (C) nel rettangolo</li>
      <li>A oltre la linea dei difensori</li>
      <li>C oltre la linea dei centrocampisti</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Quando un centrocampista riceve, il difensore di fronte <b>esce</b> su di lui e i compagni vicini si stringono alle sue spalle formando la piramide.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Uscire forte mentre la palla viaggia</li>
      <li>Chi è vicino copre subito l'uscita</li>
      <li>Non lasciare passare palla verso A</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. Rondo
def campo_rondo():
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:110mm;margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <rect x="120" y="40" width="260" height="220" fill="none" stroke="#fff" stroke-width="2.5"/>
    {g(250, 40, "pA")}{g(120, 150, "pA")}{g(380, 150, "pA")}{g(250, 260, "pA")}
    {g(205, 125, "pA")}{g(290, 185, "pA")}
    {g(180, 85, "pB")}{g(260, 175, "pB")}
    {freccia("M128,140 L196,128", tratteggio=True)}{freccia("M214,120 L242,52", tratteggio=True)}
    <use href="#palla" x="132" y="160"/>
  </svg>'''

rondo = pagina_esercizio(
    "Esercitazione III · Gruppo B", "Rondo",
    "possesso palla a pochi tocchi e pressione coordinata dei due che stanno in mezzo.",
    campo_rondo(),
    "<li>4 giocatori sui lati del quadrato</li><li>2 giocatori dentro con la squadra in possesso</li><li>2 giocatori che pressano</li>",
    "<p><b>4 serie da 3 minuti</b> con <b>2 minuti di recupero</b>.</p>"
    "<p>La squadra in possesso fa girare palla. I due in mezzo provano a recuperarla.</p>",
    "<li>Smarcarsi dentro il quadrato per dare la linea interna</li><li>Passaggi forti e precisi</li><li>Chi pressa lo fa in coppia, chiudendo una linea di passaggio</li>",
    chips='<span class="chip">20 minuti, poi cambio</span><span class="chip">4 serie da 3\'</span><span class="chip">Recupero 2\'</span>')

# ---------- 6. Parte atletica
blocchi = [("45\"-15\"", "15\" di allungo sul lato lungo, 45\" di recupero sulla diagonale"),
           ("20\"-20\"", "20\" di corsa su 100 m, 20\" di recupero"),
           ("15\"-15\"", "15\" di corsa su 80 m, 15\" di recupero"),
           ("10\"-10\"", "10\" di navetta su 16 m, 10\" di recupero")]
recupero = '<tr class="rec"><td class="min">3\'</td><td class="rit">Recupero</td><td>3 minuti di recupero prima del blocco successivo</td></tr>'
righe = recupero.join(f'<tr><td class="min">6\'</td><td class="rit">{r}</td><td>{d}</td></tr>' for r, d in blocchi)

atletica = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Parte atletica · navette</h2></div>
  <div class="ex-sub">
    <span class="chip">33 minuti</span><span class="chip">4 blocchi da 6 minuti</span><span class="chip">3 minuti di recupero tra i blocchi</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> resistenza alla velocità. Stessi blocchi dell'Allenamento 4 ma più lunghi: da 4 a 6 minuti ciascuno.</p>
  <table class="intervalli">{righe}</table>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo intero per gli allunghi</li>
      <li>Distanze segnate a 100, 80 e 16 m</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni blocco dura 6 minuti: si alterna il tratto di corsa al recupero, con i tempi indicati in tabella.</p>
      <p>Tra un blocco e l'altro <b>3 minuti di recupero</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Rispettare i tempi di partenza</li>
      <li>Nella navetta frenare e ripartire bassi</li>
      <li>Stessa intensità fino all'ultima ripetuta</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, partita, uscite, rondo, atletica]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-05.html").write_text(html)
print("pagine:", PAG[0])
