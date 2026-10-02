"""Genera allenamento-10.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 10</title>")
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
             .replace("allenamento-01.jpg", "allenamento-10.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 10")
             .replace("la prima seduta della Juniores", "la decima seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 10</span>'
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
      <h2>Allenamento 10</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">85' + suicidi</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">3/4 di campo</div></div>
    <div><div class="l">Focus</div><div class="v">Cross e partite a tema</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “cross”</div><div class="d">Corsie laterali dove si entra solo per andare al cross · 2 tempi da 15'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Parte atletica a partite</div><div class="d">3 partite da 15' su 3/4 di campo, con tocchi e punteggi diversi</div></td><td class="min">45'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Suicidi</div><div class="d">Per chi ha perso le partite</div></td><td class="min">–</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita cross · 30'</div>
    <div style="flex:45;background:var(--oro);color:var(--verde)">Atletica a partite · 45'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Una seduta tutta giocata: prima si allena il <b>cross</b>, poi la parte atletica si fa con <b>tre partite a tema</b>. Ogni partita conta, perché a fine allenamento chi ha perso paga con i suicidi.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita cross
def campo_cross():
    # campo in verticale con le corsie laterali: i blu attaccano verso l'alto (4-2-3-1)
    blu = (g(130, 330, "pB") + g(205, 335, "pB") + g(295, 335, "pB") + g(370, 330, "pB")
           + g(200, 280, "pB") + g(300, 280, "pB")
           + g(115, 205, "pB") + g(250, 215, "pB") + g(385, 205, "pB")
           + g(270, 80, "pB"))
    rossi = (g(130, 60, "pA") + g(205, 55, "pA") + g(295, 55, "pA") + g(370, 60, "pA")
             + g(200, 120, "pA") + g(300, 120, "pA")
             + g(130, 175, "pA") + g(250, 160, "pA") + g(370, 175, "pA")
             + g(240, 255, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:100mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <rect x="30" y="20" width="65" height="340" fill="#f2c230" opacity=".14"/>
    <rect x="405" y="20" width="65" height="340" fill="#f2c230" opacity=".14"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="340"/>
      <line x1="95" y1="20" x2="95" y2="360"/><line x1="405" y1="20" x2="405" y2="360"/>
      <line x1="95" y1="190" x2="405" y2="190"/>
      <rect x="215" y="6" width="70" height="14"/><rect x="215" y="360" width="70" height="14"/>
    </g>
    {g(250, 30, "pP")}{g(250, 350, "pP")}
    {rossi}{blu}
    {freccia("M118,192 L62,120", True)}{freccia("M62,104 Q150,40 258,76", tratteggio=True)}
    <use href="#palla" x="70" y="112"/>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1" text-anchor="middle">
      <text x="62" y="300" transform="rotate(-90 62 300)">CORSIA</text>
      <text x="437" y="300" transform="rotate(-90 437 300)">CORSIA</text>
    </g>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “cross”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Corsie laterali</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> cercare il compagno sulla fascia che va al cross. Nella corsia si entra solo per crossare.</p>
  {campo_cross()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li>Ricerca di un giocatore sulla <b>fascia</b> che va al cross</li>
        <li><b>Non si può stare nella corsia</b>: ci si entra solo per andare al cross</li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Ricerca di un giocatore <b>in corsia</b> per il cross</li>
        <li>Anche qui nella corsia si entra <b>solo per andare al cross</b></li>
        <li>Se su una <b>ripartenza</b> un giocatore stoppa la palla e si gira libero: <b>1 punto</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo con due corsie laterali segnate</li>
      <li>Due squadre da 10 con il 4-2-3-1</li>
      <li>Due porte con i portieri</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita con porte. Si costruisce al centro e si cerca il compagno che entra in corsia e crossa.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Entrare in corsia nel momento giusto, non prima</li>
      <li>In area attaccare il primo e il secondo palo</li>
      <li>Chi difende si sistema in diagonale invertita</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Parte atletica a partite + suicidi
righe = "".join(f'<tr><td class="min">{m}</td><td class="rit">{t}</td><td>{d}</td></tr>' for m, t, d in [
    ("15'", "Partita 1", "<b>3 tocchi</b> · gol valido solo se tutti sono nella metà offensiva · gol con palla recuperata nella metà offensiva: <b>doppio</b>"),
    ("15'", "Partita 2", "<b>2 tocchi</b> · gol valido solo se tutti sono nella metà offensiva · <b>doppio</b> se un giocatore della squadra che difende è rimasto nella sua metà offensiva · gol con palla recuperata nella metà offensiva: <b>doppio</b>"),
    ("5'", "Partita 3 · a", "<b>3 tocchi</b> · gol valido solo se tutti sono nella metà offensiva"),
    ("5'", "Partita 3 · b", "<b>2 tocchi</b> · gol valido solo se tutti sono nella metà offensiva · <b>doppio</b> se fatto in 4 passaggi dopo aver recuperato palla nella metà difensiva"),
    ("5'", "Partita 3 · c", "<b>1 tocco</b> · gol <b>doppio</b> se si recupera palla e si segna in 4 passaggi"),
])

atletica = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Parte atletica a partite</h2></div>
  <div class="ex-sub">
    <span class="chip">45 minuti</span><span class="chip">3 partite da 15'</span><span class="chip">3/4 di campo</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> fare la parte atletica giocando. L'intensità arriva dai pochi tocchi e dai punteggi che premiano la pressione e la verticalità.</p>
  <table class="intervalli">{righe}</table>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>3/4 di campo diviso in due metà</li>
      <li>Due squadre con il 4-2-3-1</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Tre partite di fila. L'ultima è divisa in tre parti da 5', con i tocchi che scendono da 3 a 1.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Salire tutti insieme</li>
      <li>Dopo il recupero, verticalizzare in pochi passaggi</li>
      <li>Ritmo alto fino all'ultimo minuto</li>
    </ul></div>
  </div>

  <div class="chiave">
    <span class="kicker">Esercitazione IV · suicidi per chi ha perso le partite</span>
    Per ogni partita: sconfitta <b>5 suicidi</b> · pareggio <b>3</b> · vittoria <b>1</b>. Se una squadra perde tutte e 4 le partite fa <b>20 suicidi</b>.
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, partita, atletica]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-10.html").write_text(html)
print("pagine:", PAG[0])
