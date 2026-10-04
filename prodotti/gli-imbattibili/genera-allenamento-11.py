"""Genera allenamento-11.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 11</title>")
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
             .replace("allenamento-01.jpg", "allenamento-11.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 11")
             .replace("la prima seduta della Juniores", "l'undicesima seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 11</span>'
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
      <h2>Allenamento 11</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">1 ora + suicidi</div></div>
    <div><div class="l">Giocatori</div><div class="v">16 per campo</div></div>
    <div><div class="l">Campo</div><div class="v">20 × 20 m</div></div>
    <div><div class="l">Focus</div><div class="v">Rapidità e gioco con le sponde</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Rapidità a stazioni</div><div class="d">4 stazioni, ognuna chiusa da 10 m di sprint · 8 volte per stazione</div></td><td class="min">20'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Partita 4 contro 4 con 4 sponde</div><div class="d">Campo 20 × 20 · 2 tocchi, sponde a 1 tocco · gol valido solo su passaggio della sponda · serie da 5'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Suicidi</div><div class="d">Per chi ha perso la partita</div></td><td class="min">–</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:20;background:var(--oro);color:var(--verde)">Rapidità · 20'</div>
    <div style="flex:30;background:var(--verde-2)">4 contro 4 + sponde · 30'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Una seduta corta e intensa, di un'ora: prima la <b>rapidità</b>, poi una partita in spazi stretti dove si segna solo <b>passando dalla sponda</b>. Chi gioca deve cercare il compagno fuori dal campo e attaccare subito la porta.
  </div>
  {footer()}
</section>'''

# ---------- 3. Rapidità a stazioni
stazioni = [
    ("Skip + sprint", "5 m di skip, poi 10 m di sprint", "8 volte"),
    ("Scaletta + sprint", "scaletta, poi 10 m di sprint", "8 volte"),
    ("Slalom + sprint", "slalom tra 4 paletti, poi 10 m di sprint", "8 volte"),
    ("Salto + sprint", "salto sul posto da mezzo squat, poi 10 m di sprint", "8 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    + (f'<div class="d">{d}</div>' if d else "") + f'</div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Rapidità a stazioni</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti</span><span class="chip">4 stazioni</span><span class="chip">8 volte per stazione</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità e reattività. Come negli Allenamenti 7 e 9 ogni stazione finisce con uno sprint di 10 metri, ma le ripetizioni salgono a 8.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>4 stazioni in sequenza</li>
      <li>4 paletti, una scaletta, 10 m segnati dopo ogni stazione</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si fanno le 8 ripetizioni di una stazione e si passa alla successiva, dalla 1 alla 4.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Massima velocità in ogni sprint</li>
      <li>Dal mezzo squat spingere forte e ripartire subito</li>
      <li>Recuperare completamente prima della ripetizione successiva</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Partita 4 contro 4 con 4 sponde
def campo_sponde():
    # rossi (X) attaccano verso l'alto con le sponde intorno alla porta alta; blu (O) verso il basso
    dentro = (g(180, 120, "pB") + g(320, 120, "pB") + g(180, 260, "pB") + g(320, 260, "pB")
              + g(200, 150, "pA") + g(300, 150, "pA") + g(200, 230, "pA") + g(300, 230, "pA"))
    sponde_rosse = g(150, 22, "pA") + g(350, 22, "pA") + g(78, 120, "pA") + g(422, 120, "pA")
    sponde_blu = g(150, 358, "pB") + g(350, 358, "pB") + g(78, 260, "pB") + g(422, 260, "pB")
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:112mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="100" y="40" width="300" height="300"/>
      <line x1="100" y1="190" x2="400" y2="190"/>
      <rect x="220" y="28" width="60" height="12"/><rect x="220" y="340" width="60" height="12"/>
    </g>
    <text x="250" y="374" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">20 × 20 M</text>
    {dentro}{sponde_rosse}{sponde_blu}
    {freccia("M212,226 L408,128", tratteggio=True)}{freccia("M412,112 L264,44", tratteggio=True)}
    <use href="#palla" x="214" y="244"/>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="40" y="96">SPONDA</text><text x="436" y="96">SPONDA</text>
    </g>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Partita 4 contro 4 con 4 sponde</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · serie da 5'</span><span class="chip">4 contro 4 + 4 sponde per squadra</span><span class="chip">Campo 20 × 20 m</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> giocare in spazi stretti e veloci usando il compagno fuori dal campo. Il gol vale solo se l'ultimo passaggio arriva dalla sponda.</p>
  {campo_sponde()}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Quadrato di 20 × 20 m con due porte piccole</li>
      <li>4 contro 4 dentro il campo</li>
      <li>Ogni squadra ha 4 sponde fuori: due ai lati della porta che attacca e due sulle linee laterali</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si gioca a <b>2 tocchi</b>, le sponde a <b>1 tocco</b>.</p>
      <p>Il gol è valido solo se arriva <b>su passaggio della sponda</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Cercare subito la sponda libera</li>
      <li>Attaccare la porta appena la palla torna dentro</li>
      <li>Chi difende chiude prima la linea verso la sponda</li>
    </ul></div>
  </div>

  <div class="chiave">
    <span class="kicker">Esercitazione IV · suicidi a fine allenamento</span>
    Chi perde: <b>5 suicidi</b> · chi vince: <b>1 suicidio</b> · pareggio: <b>3 suicidi a testa</b>.
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, rapidita, partita]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-11.html").write_text(html)
print("pagine:", PAG[0])
