"""Genera allenamento-15.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 15
TESTO_PIEDE = f"In campionato · Allenamento {N}"

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      f"<title>Gli Imbattibili – In campionato, Allenamento {N}</title>")
# stili in più: stazioni (come nell'Allenamento 11) e pagina della partita
testa = testa.replace("</style>\n</head>", """.stazioni { display: grid; grid-template-columns: 1fr; gap: 3mm; margin: 2mm 0 5mm; }
.stazione { display: flex; gap: 4mm; align-items: center; background: #f3f5f2; border-radius: 2mm; padding: 3.5mm 4mm; }
.stazione .n { flex: none; width: 10mm; height: 10mm; border-radius: 50%; background: var(--verde); color: var(--oro); font-family: Oswald, sans-serif; font-weight: 700; font-size: 15pt; display: flex; align-items: center; justify-content: center; }
.stazione .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 12pt; letter-spacing: .02em; line-height: 1.2; }
.stazione .d { font-size: 9.5pt; color: #5d6b65; margin-top: .5mm; }
.stazione .q { margin-left: auto; flex: none; font-family: Oswald, sans-serif; font-size: 13pt; color: var(--verde); font-weight: 700; text-align: right; }
.tabellone { background: var(--verde); color: #fff; border-radius: 3mm; padding: 9mm 8mm 7mm; margin: 6mm 0 7mm; text-align: center; }
.tabellone .sq { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 6mm; }
.tabellone .nome { font-family: Oswald, sans-serif; text-transform: uppercase; font-size: 15pt; line-height: 1.15; letter-spacing: .02em; }
.tabellone .nome.noi { color: var(--oro); }
.tabellone .ris { font-family: Oswald, sans-serif; font-weight: 700; font-size: 46pt; line-height: 1; }
.tabellone .tempi { margin-top: 4mm; font-size: 10pt; color: #b9cfc4; letter-spacing: .04em; }
.stat { width: 100%; border-collapse: collapse; }
.stat td { padding: 2.2mm 0; font-size: 10pt; vertical-align: middle; }
.stat .v { font-family: Oswald, sans-serif; font-size: 14pt; width: 12mm; color: var(--verde); }
.stat .v.dx { text-align: right; }
.stat .lab { text-align: center; font-size: 9.5pt; color: #5d6b65; padding-bottom: 1mm; }
.stat .barra { display: flex; height: 3mm; gap: 1mm; }
.stat .barra div { border-radius: 1mm; }
</style>
</head>""", 1)
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("precampionato/allenamento-01.jpg", f"campionato/allenamento-{N}.jpg")
             .replace("Precampionato · Allenamento 1", TESTO_PIEDE)
             .replace("la prima seduta della Juniores",
                      "la seduta del giovedì della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>{TESTO_PIEDE}</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


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
      <div class="kicker">In campionato · Seduta del giovedì</div>
      <h2>Allenamento {N}</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 76' + suicidi</div></div>
    <div><div class="l">Giocatori</div><div class="v">Due squadre · 2 contro 2</div></div>
    <div><div class="l">Campo</div><div class="v">3/4 di campo · campo ridotto</div></div>
    <div><div class="l">Focus</div><div class="v">Pressione, preventive e rapidità</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione generale</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita a pressione con preventive</div><div class="d">3/4 di campo · 2 tempi da 15' con le stesse regole · 2 tocchi · gol doppio con regole diverse per le due squadre</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Rapidità a stazioni</div><div class="d">4 stazioni · 5 volte per stazione · l'ultima a coppie</div></td><td class="min">15'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">2 contro 2 a partita</div><div class="d">Chi vince resta · 4 serie da 1'30" · chi perde fa i suicidi a fine allenamento</div></td><td class="min">6'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita libera</div><div class="d">Poi i suicidi per chi ha perso il 2 contro 2</div></td><td class="min">15'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Pressione · 30'</div>
    <div style="flex:15;background:var(--oro);color:var(--verde)">Rapidità · 15'</div>
    <div style="flex:6;background:var(--verde)">2c2</div>
    <div style="flex:15;background:var(--verde-2)">Partita · 15'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il giovedì si lavora sulla <b>pressione</b>: una squadra è premiata se attacca in fretta dopo il recupero,
    l'altra se recupera palla nella metà campo avversaria. Chi non pressa resta scoperto, per questo servono le
    <b>preventive</b>. Poi rapidità, un 2 contro 2 dove chi perde paga e la partita libera.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita a pressione con preventive
pressione_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:96mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="60" y="22" width="380" height="336"/>
      <line x1="60" y1="190" x2="440" y2="190"/>
      <rect x="205" y="10" width="90" height="12"/><rect x="205" y="358" width="90" height="12"/>
    </g>
    <rect x="60" y="10" width="46" height="12" fill="#f2c230"/><rect x="394" y="10" width="46" height="12" fill="#f2c230"/>
    <g font-family="Oswald" font-size="10" fill="#f2c230" letter-spacing="1" text-anchor="middle">
      <text x="83" y="36">PORTICINA</text><text x="417" y="36">PORTICINA</text>
    </g>
    {g(250, 36, "pP")}{g(250, 344, "pP")}
    <g font-family="Oswald" font-weight="700" text-anchor="middle">
      <text x="250" y="125" font-size="64" fill="#2a5db0" stroke="#fff" stroke-width="1.5">B</text>
      <text x="250" y="295" font-size="64" fill="#c8372d" stroke="#fff" stroke-width="1.5">A</text>
    </g>
    {freccia("M160,80 L160,150", tratteggio=True)}{freccia("M340,80 L340,150", tratteggio=True)}
    {freccia("M160,300 L160,230", oro=True)}{freccia("M340,300 L340,230", oro=True)}
  </svg>'''

pressione = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita a pressione con preventive</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">Stesse regole nei due tempi</span><span class="chip">3/4 di campo</span><span class="chip">2 tocchi</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> pressare e attaccare subito dopo il recupero. Le due squadre hanno regole diverse: chi attacca in fretta da una parte, chi recupera alto dall'altra. Per non farsi sorprendere bisogna tenere le marcature preventive.</p>
  <div style="display:flex;gap:5mm;align-items:center">
    <div style="flex:1">{pressione_svg}</div>
    <div style="flex:1;display:flex;flex-direction:column;gap:3mm">
      <div class="box"><h4>Squadra A · attacca in alto</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li>
        <li>Si segna nella porta o <b>attraversando le porticine laterali</b></li>
        <li>Se ci arriva con <b>massimo 4 passaggi</b> dal recupero o dalla ripartenza del portiere: <b>gol doppio</b></li></ul></div>
      <div class="box"><h4>Squadra B · attacca in basso</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li>
        <li>Se <b>recupera palla nella metà offensiva</b> e segna: <b>gol doppio</b></li></ul></div>
    </div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>3/4 di campo con due porte e i portieri</li>
      <li>Due porticine laterali ai lati della porta che attacca la squadra A</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Due tempi da 15' con le stesse regole: la squadra A cerca di attaccare in pochi passaggi, la squadra B di riconquistare palla nella metà campo avversaria.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Chi attacca lascia sempre qualcuno in marcatura preventiva</li>
      <li>Dopo il recupero, verticalizzare subito</li>
      <li>Chi perde palla aggredisce subito</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Rapidità a stazioni
stazioni = [
    ("Skip + scatto", "5 m di skip (alto, dietro, basso, destro e sinistro), poi 10 m di scatto", "5 volte"),
    ("Scaletta + scatto", "scaletta, poi 10 m di scatto", "5 volte"),
    ("Scatto con arresto", "7 m di scatto, arresto al cono, altri 7 m di scatto", "5 volte"),
    ("Sfida a coppie", "10 m di scatto fino ai conetti, poi 5 m: chi passa per secondo tra i conetti continua lo scatto. Il via lo dà la coppia dietro", "5 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    f'<div class="d">{d}</div></div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Rapidità a stazioni</h2></div>
  <div class="ex-sub">
    <span class="chip">4 stazioni</span><span class="chip">5 volte per stazione</span><span class="chip">L'ultima a coppie</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità, cambi di ritmo e arresti. Ogni stazione finisce con uno scatto, l'ultima è una sfida a coppie.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Una scaletta, coni per l'arresto, conetti per la sfida a coppie</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si fanno le 5 ripetizioni di una stazione e si passa alla successiva.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Nell'arresto abbassare il baricentro e ripartire subito</li>
      <li>Massima velocità in ogni scatto</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. 2 contro 2 + partita libera
duecontrodue_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:88mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="110" y="40" width="280" height="300"/>
      <rect x="215" y="28" width="70" height="12"/><rect x="215" y="340" width="70" height="12"/>
    </g>
    {g(250, 54, "pP")}{g(250, 326, "pP")}
    {g(190, 130, "pA")}{g(310, 130, "pA")}{g(200, 250, "pB")}{g(300, 250, "pB")}
    {g(180, 14, "pA")}{g(180, 34, "pA")}{g(320, 14, "pA")}{g(320, 34, "pA")}
    {g(180, 346, "pB")}{g(180, 366, "pB")}{g(320, 346, "pB")}{g(320, 366, "pB")}
    <use href="#palla" x="320" y="142"/>
    {freccia("M300,240 L275,215", oro=True)}
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="342" y="28">IN ATTESA</text><text x="342" y="360">IN ATTESA</text>
    </g>
  </svg>'''

duecontrodue = pagina_esercizio(
    "Esercitazione IV", "2 contro 2 a partita · chi vince resta",
    "duelli continui a tocco libero: chi segna resta in campo, chi subisce gol lascia il posto a un'altra coppia.",
    duecontrodue_svg,
    "<li>Campo ridotto con due porte e i portieri</li><li>Le coppie di ogni squadra aspettano il loro turno dietro la propria porta</li>",
    "<p>Tocco libero, <b>4 serie da 1'30\"</b>.</p><p><b>Chi segna resta in campo</b> e si fa dare la palla dal proprio portiere. "
    "<b>Chi subisce gol esce</b> ed entrano altri 2.</p>",
    "<li>Attaccare subito la porta</li><li>In due: uno attacca la palla, l'altro copre</li>",
    '<span class="chip">4 serie da 1\'30"</span><span class="chip">2 contro 2 + portieri</span><span class="chip">Tocco libero</span>')
duecontrodue = duecontrodue.replace("  <div class=\"footer\">", '''  <div class="chiave">
    <span class="kicker">Suicidi a fine allenamento · Esercitazione V · partita libera 15'</span>
    Chi perde il 2 contro 2: <b>5 suicidi</b> · in caso di parità: <b>3 suicidi</b>. Prima dei suicidi, <b>15' di partita libera</b>.
  </div>
  <div class="footer">''', 1)


# ---------- 6. La partita del fine settimana
def pagina_partita(casa, ospiti, gol, primo, secondo, stat, noi="dx"):
    righe = ""
    for lab, a, b in stat:
        tot = (a + b) or 1
        ca, cb = ("#c9d3ce", "var(--oro)") if noi == "dx" else ("var(--oro)", "#c9d3ce")
        righe += (f'<tr><td class="v">{a}</td><td><div class="lab">{lab}</div><div class="barra">'
                  f'<div style="flex:{a / tot:.3f};background:{ca}"></div>'
                  f'<div style="flex:{b / tot:.3f};background:{cb}"></div></div></td>'
                  f'<td class="v dx">{b}</td></tr>')
    cl_a, cl_b = ("nome", "nome noi") if noi == "dx" else ("nome noi", "nome")
    return f'''<section class="page">
  <div class="kicker">Il fine settimana</div>
  <div class="ex-title"><h2>La partita</h2></div>
  <p class="obj">Dopo le sedute del lunedì e del giovedì, il risultato della partita.</p>
  <div class="tabellone">
    <div class="sq">
      <div class="{cl_a}">{casa}</div>
      <div class="ris">{gol[0]} – {gol[1]}</div>
      <div class="{cl_b}">{ospiti}</div>
    </div>
    <div class="tempi">PRIMO TEMPO {primo[0]} – {primo[1]} · SECONDO TEMPO {secondo[0]} – {secondo[1]}</div>
  </div>
  <h3>Statistiche</h3>
  <table class="stat">{righe}</table>
  {footer()}
</section>'''


risultato = pagina_partita(
    "Spartaco Banti Barberino", "Fiesole", (1, 0), (1, 0), (0, 0),
    [("Tiri in porta", 3, 2), ("Tiri fuori porta", 3, 7), ("Calci d'angolo", 1, 5), ("Fuorigioco", 2, 3),
     ("Falli", 22, 24), ("Cartellini gialli", 5, 4), ("Cartellini rossi", 0, 0), ("Calci di rinvio", 8, 5)],
    noi="sx")

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, pressione, rapidita, duecontrodue, risultato]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
