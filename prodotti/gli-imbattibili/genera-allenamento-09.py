"""Genera allenamento-09.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 9</title>")
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
             .replace("allenamento-01.jpg", "allenamento-09.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 9")
             .replace("la prima seduta della Juniores", "la nona seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 9</span>'
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
      <div class="kicker">Precampionato · Settimana 3</div>
      <h2>Allenamento 9</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">90-95'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">Diviso in 2 metà</div></div>
    <div><div class="l">Focus</div><div class="v">Pressione e rapidità</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Rapidità a stazioni</div><div class="d">4 stazioni, ognuna chiusa da 10 m di scatto · 5 volte per stazione</div></td><td class="min">20'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Partita a pressione</div><div class="d">2 tocchi · il recupero nella metà offensiva vale doppio · gol valido solo se tutti sono nella metà offensiva · 2 tempi da 15'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Angoli difensivi</div><div class="d">Lavoro sui calci d'angolo a sfavore</div></td><td class="min">20'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita libera</div><div class="d">Senza vincoli</div></td><td class="min">10-15'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:20;background:var(--oro);color:var(--verde)">Rapidità · 20'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:20;background:var(--verde)">Angoli · 20'</div>
    <div style="flex:12;background:#7aa995">10-15'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Si torna sulla <b>pressione con la squadra corta</b>: il recupero alto vale doppio e nel 2° tempo è premiato anche chi segna prima che l'avversario sia rientrato. Prima, la rapidità prepara le gambe agli scatti brevi.
  </div>
  {footer()}
</section>'''

# ---------- 3. Rapidità a stazioni
stazioni = [
    ("Slalom + scatto", "slalom su 5 paletti, poi 10 m di scatto", "5 volte"),
    ("Scaletta + scatto", "scaletta, poi 10 m di scatto", "5 volte"),
    ("Skip + scatto", "5 m di skip, poi 10 m di scatto", "5 volte"),
    ("Salto + scatto", "salto sul posto, poi 10 m di scatto", "5 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    + (f'<div class="d">{d}</div>' if d else "") + f'</div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Rapidità a stazioni</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti</span><span class="chip">4 stazioni</span><span class="chip">5 volte per stazione</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità e reattività. Come nell'Allenamento 7, ogni stazione finisce con uno scatto di 10 metri.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>4 stazioni in sequenza</li>
      <li>5 paletti, una scaletta, 10 m segnati dopo ogni stazione</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si fanno le 5 ripetizioni di una stazione e si passa alla successiva, dalla 1 alla 4.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Massima velocità in ogni scatto</li>
      <li>Dopo il salto ripartire subito</li>
      <li>Recuperare completamente prima della ripetizione successiva</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Partita a pressione
def campo_partita():
    # campo in verticale: i blu attaccano verso l'alto, tutti nella metà offensiva (4-2-3-1)
    blu = (g(110, 172, "pB") + g(200, 175, "pB") + g(300, 175, "pB") + g(390, 172, "pB")
           + g(195, 140, "pB") + g(305, 140, "pB")
           + g(90, 100, "pB") + g(250, 100, "pB") + g(410, 100, "pB")
           + g(330, 62, "pB"))
    rossi = (g(110, 48, "pA") + g(200, 45, "pA") + g(290, 45, "pA") + g(390, 48, "pA")
             + g(200, 82, "pA") + g(300, 82, "pA")
             + g(130, 132, "pA") + g(250, 150, "pA") + g(370, 132, "pA")
             + g(250, 255, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:100mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <rect x="30" y="20" width="440" height="170" fill="#f2c230" opacity=".12"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="340"/>
      <line x1="30" y1="190" x2="470" y2="190"/>
      <rect x="215" y="6" width="70" height="14"/><rect x="215" y="360" width="70" height="14"/>
    </g>
    {g(250, 30, "pP")}{g(250, 350, "pP")}
    {rossi}{blu}
    {freccia("M240,108 L250,136", True)}
    <use href="#palla" x="262" y="158"/>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="40" y="206">METÀ OFFENSIVA BLU ↑ · TUTTI DENTRO</text>
      <text x="275" y="260">ROSSO NON RIENTRATO</text>
    </g>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Partita a pressione</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Diviso in 2 metà</span><span class="chip">2 tocchi</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> pressare con la squadra corta e recuperare palla nella metà avversaria. Nel 2° tempo si punisce chi non è rientrato.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Gol dopo un <b>recupero nella metà offensiva</b>: <b>2 punti</b></li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Gol dopo un <b>recupero nella metà offensiva</b>: <b>2 punti</b></li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
        <li><b>Gol doppio</b> se gli avversari non sono tutti nella propria metà difensiva</li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo diviso in due metà</li>
      <li>Due squadre da 10 con il 4-2-3-1</li>
      <li>Due porte con i portieri</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita con porte a 2 tocchi. Si segna solo con tutta la squadra nella metà offensiva.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Salire tutti insieme, anche i difensori</li>
      <li>Persa palla, rientrare subito nella propria metà</li>
      <li>Pressare forte per recuperare in avanti</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. Angoli difensivi + partita libera
finale = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Angoli difensivi · 20'</h2></div>
  <div class="box" style="margin-top:4mm">Lavoro sui calci d'angolo a sfavore. Marcature e posizioni in area: ogni allenatore le organizza come preferisce.</div>

  <div class="kicker" style="margin-top:9mm">Esercitazione V</div>
  <div class="ex-title"><h2>Partita libera · 10-15'</h2></div>
  <div class="box" style="margin-top:4mm">Partita a fine seduta senza vincoli di tocchi o di punteggio.</div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, rapidita, partita, finale]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-09.html").write_text(html)
print("pagine:", PAG[0])
