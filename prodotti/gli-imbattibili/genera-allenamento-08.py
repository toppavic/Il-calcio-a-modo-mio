"""Genera allenamento-08.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 8</title>")
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
             .replace("allenamento-01.jpg", "allenamento-08.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 8")
             .replace("la prima seduta della Juniores", "l'ottava seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 8</span>'
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
      <h2>Allenamento 8</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 110'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">3/4 di campo</div></div>
    <div><div class="l">Focus</div><div class="v">Preventive e ripartenze</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “ultimo passaggio”</div><div class="d">Campo diviso in due parti in verticale · gol doppio se nasce da un passaggio da una metà all'altra · 2 tempi da 15'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Attacco contro difesa in emergenza</div><div class="d">Sequenze di uscita: chi esce gira intorno ai paletti e rientra mentre la squadra difende la ripartenza · 2 tempi da 15-20'</div></td><td class="min">30-40'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Parte atletica · navette</div><div class="d">Intermittente a tempi decrescenti · blocchi da 7', 7', 7' e 6' con 3' di recupero</div></td><td class="min">36'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:35;background:var(--verde)">Emergenza · 30-40'</div>
    <div style="flex:36;background:var(--oro);color:var(--verde)">Atletica · 36'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Si lavora su cosa succede <b>quando si perde palla</b>: in partita è premiato il recupero pulito, nell'attacco contro difesa la squadra deve difendersi in emergenza mentre chi era uscito <b>rientra di corsa</b>. Controllare le preventive e le ripartenze.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita ultimo passaggio
def campo_partita():
    # campo in verticale: i blu attaccano verso l'alto, i rossi verso il basso (4-2-3-1)
    blu = (g(110, 320, "pB") + g(200, 325, "pB") + g(300, 325, "pB") + g(390, 320, "pB")
           + g(195, 270, "pB") + g(305, 270, "pB")
           + g(90, 210, "pB") + g(250, 215, "pB") + g(410, 210, "pB")
           + g(330, 150, "pB"))
    rossi = (g(110, 60, "pA") + g(200, 55, "pA") + g(300, 55, "pA") + g(390, 60, "pA")
             + g(195, 110, "pA") + g(305, 110, "pA")
             + g(90, 170, "pA") + g(250, 165, "pA") + g(410, 170, "pA")
             + g(170, 225, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:100mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <rect x="30" y="20" width="220" height="340" fill="#f2c230" opacity=".10"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="340"/>
      <line x1="250" y1="20" x2="250" y2="360"/>
      <rect x="215" y="6" width="70" height="14"/><rect x="215" y="360" width="70" height="14"/>
    </g>
    {g(250, 30, "pP")}{g(250, 350, "pP")}
    {rossi}{blu}
    {freccia("M98,204 L318,154", tratteggio=True)}{freccia("M330,138 L262,44", tratteggio=True)}
    <use href="#palla" x="96" y="222"/>
    <text x="140" y="374" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">METÀ SINISTRA</text>
    <text x="360" y="374" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">METÀ DESTRA</text>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “ultimo passaggio”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Diviso in 2 parti in verticale</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> cercare l'ultimo passaggio che cambia lato. Il gol vale doppio se arriva dopo un passaggio da una metà all'altra.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Campo diviso in <b>2 parti in verticale</b></li>
        <li>Massimo <b>3 tocchi</b></li>
        <li>Gol segnato con un <b>passaggio da una metà all'altra</b>: <b>vale doppio</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li>Gol segnato con un <b>passaggio da una metà all'altra</b>: <b>vale doppio</b></li>
        <li>Se il <b>passaggio dopo il recupero palla</b> esce pulito: <b>1 punto</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo diviso a metà nel senso della lunghezza</li>
      <li>Due squadre da 10 con il 4-2-3-1</li>
      <li>Due porte con i portieri</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita con porte. Si attira l'avversario su un lato e poi si cambia metà con l'ultimo passaggio.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Attirare da una parte, colpire dall'altra</li>
      <li>Chi è sul lato debole si fa trovare pronto</li>
      <li>Dopo il recupero il primo passaggio deve essere pulito</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Attacco contro difesa in emergenza
oro = lambda x, y: f'<circle cx="{x}" cy="{y}" r="17" fill="none" stroke="#f2c230" stroke-width="3"/>'
paletti = "".join(f'<rect x="{x-3}" y="356" width="6" height="16" rx="2" fill="#f2c230"/>' for x in (160, 210, 290, 340))
emergenza_svg = mezzo_campo(
    paletti
    + '<text x="250" y="352" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">PALETTI SUI 3/4</text>'
    + oro(110, 150) + oro(90, 265) + oro(410, 265) + oro(250, 280) + oro(250, 320)
    + g(110, 150, "pB", 2) + g(200, 150, "pB", 5) + g(300, 150, "pB", 6) + g(390, 150, "pB", 3)
    + g(200, 215, "pB", 4) + g(300, 215, "pB", 8)
    + g(90, 265, "pB", 7) + g(250, 280, "pB", 10) + g(410, 265, "pB", 11) + g(250, 320, "pB", 9)
    + g(40, 345, "pA", "XL") + g(460, 345, "pA", "XL")
    + g(250, 95, "pA") + g(250, 218, "pA") + g(195, 285, "pA") + g(305, 285, "pA") + g(45, 195, "pA") + g(455, 195, "pA")
    + freccia("M92,280 L52,334", tratteggio=True) + freccia("M48,332 L184,288", tratteggio=True)
    + '<use href="#palla" x="86" y="282"/>', "112mm")

righe_seq = "".join(f'<tr><td class="min">{n}</td><td>{t}</td></tr>' for n, t in [
    ("1", "Escono i <b>2 laterali d'attacco</b>, il <b>trequartista</b>, la <b>punta</b> e <b>un terzino</b>"),
    ("2", "Escono i <b>2 laterali d'attacco</b>, il <b>trequartista</b>, la <b>punta</b> e <b>un centrocampista</b>"),
    ("3", "Escono <b>un terzino</b>, il <b>laterale opposto</b>, il <b>trequartista</b>, la <b>punta</b> e <b>un centrocampista</b>"),
])

emergenza = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Attacco contro difesa in emergenza</h2></div>
  <div class="ex-sub">
    <span class="chip">2 tempi da 15-20'</span><span class="chip">3/4 di campo</span><span class="chip">3 sequenze di uscita</span><span class="chip">Conduce l'allenatore</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> controllare le preventive e le ripartenze. La squadra deve difendersi in inferiorità mentre chi è uscito rientra di corsa.</p>
  {emergenza_svg}
  <table class="intervalli" style="margin:3mm 0 3mm">{righe_seq}</table>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>3/4 di campo con i paletti sulla linea dei 3/4</li>
      <li>Due giocatori XL larghi in fondo al campo</li>
      <li>In oro nello schema: la sequenza 1</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Il laterale porta palla fino all'<b>XL</b> e tutta la squadra sale. L'XL scarica su un compagno e attacca: la squadra si difende in emergenza.</p>
      <p>I giocatori della sequenza girano intorno ai paletti e <b>rientrano velocemente</b> ad aiutare.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Chi resta dietro controlla le preventive</li>
      <li>Rallentare la ripartenza finché arrivano i compagni</li>
      <li>Rientrare alla massima velocità</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. Parte atletica
blocchi = [("7'", "45\"-15\"", "15\" di allungo sul lato lungo, 45\" di recupero sulla diagonale"),
           ("7'", "20\"-20\"", "20\" di corsa su 100 m, 20\" di recupero"),
           ("7'", "15\"-15\"", "15\" di corsa su 80 m, 15\" di recupero"),
           ("6'", "10\"-10\"", "10\" di navetta su 16 m, 10\" di recupero")]
recupero = '<tr class="rec"><td class="min">3\'</td><td class="rit">Recupero</td><td>3 minuti di recupero prima del blocco successivo</td></tr>'
righe = recupero.join(f'<tr><td class="min">{m}</td><td class="rit">{r}</td><td>{d}</td></tr>' for m, r, d in blocchi)

atletica = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Parte atletica · navette</h2></div>
  <div class="ex-sub">
    <span class="chip">36 minuti</span><span class="chip">Blocchi da 7', 7', 7' e 6'</span><span class="chip">3 minuti di recupero tra i blocchi</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> resistenza alla velocità. Stessi blocchi degli Allenamenti 4 e 5, ancora più lunghi.</p>
  <table class="intervalli">{righe}</table>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo intero per gli allunghi</li>
      <li>Distanze segnate a 100, 80 e 16 m</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>In ogni blocco si alterna il tratto di corsa al recupero, con i tempi indicati in tabella.</p>
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
        + "\n\n".join([scheda, partita, emergenza, atletica]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-08.html").write_text(html)
print("pagine:", PAG[0])
