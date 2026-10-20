"""Genera percorso-ricerca-del-portiere.html: Dai quaderni del mister · Percorso 1 · La ricerca del portiere.

Contenuto: pacchetto editoriale e tecnico mandato dall'allenatore il 20/10 (sezioni B-H), copiato in
prodotti/percorsi/ricerca-del-portiere/pacchetto-editoriale.md. Nome della serie: "Dai quaderni del mister"
(non "Gli Imbattibili", che resta il libro). Punti: 1 portiere trovato, 2 gol vero dopo riconquista nella metà
offensiva (il portiere para), 3 passaggio diretto dalla propria metà difensiva al portiere bersaglio.
Uso: python3 genera-percorso-ricerca-portiere.py  poi  render.js sul file .html
"""
import pathlib

QUI = pathlib.Path(__file__).parent
a2 = (QUI / "allenamento-02.html").read_text()
PIEDE = "Percorso 1 · La ricerca del portiere"

testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Dai quaderni del mister – La ricerca del portiere</title>")
testa = testa.replace("</style>\n</head>", """
.cop { background: #0b1d15; color: #fff; padding: 0 !important; }
.cop .campo { position: absolute; left: 20mm; top: 86mm; width: 170mm; }
.cop .logo { position: absolute; top: 12mm; left: 50%; transform: translateX(-50%); width: 88mm; }
.cop .txt { position: absolute; left: 20mm; right: 20mm; bottom: 18mm; }
.cop .kick { font-family: Oswald, sans-serif; font-weight: 500; letter-spacing: .22em; text-transform: uppercase; font-size: 9.5pt; color: #d4a017; }
.cop h1 { font-family: Oswald, sans-serif; font-weight: 700; text-transform: uppercase; line-height: .95; font-size: 48pt; margin: 3mm 0 3mm; }
.cop h1 span { color: #d4a017; display: block; }
.cop .claim { font-family: Oswald, sans-serif; font-size: 15pt; color: #84b94a; margin-bottom: 3mm; }
.cop .sub { font-size: 11pt; color: #d9e3dc; line-height: 1.5; margin-bottom: 2mm; }
.cop .sub b { color: #fff; }
.testo p { font-size: 10.4pt; line-height: 1.58; margin-bottom: 3mm; }
.fasi3 { display: grid; gap: 3mm; margin-top: 3mm; }
.fasi3 .box h4 { color: #9a7410; }
.fasi3 li, .elenco li { margin-bottom: 1.2mm; font-size: 9.8pt; }
.principio { margin-top: 4mm; background: var(--verde); color: #fff; border-radius: 2mm; padding: 4mm 5mm; font-size: 10pt; }
.principio b { color: var(--oro); font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .06em; display: block; margin-bottom: 1mm; }
.punto { display: grid; grid-template-columns: 14mm 1fr; gap: 3mm; align-items: start; padding: 3mm 0; border-bottom: 1px solid #e3e8e5; font-size: 9.6pt; }
.punto .v { font-family: Oswald, sans-serif; font-size: 26pt; color: var(--oro); line-height: 1; text-align: center; background: var(--verde); border-radius: 2mm; padding: 1.5mm 0; }
.punto h4 { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 11pt; margin-bottom: .5mm; }
.tab { width: 100%; border-collapse: collapse; margin-top: 2mm; font-size: 9.4pt; }
.tab th { font-family: Oswald, sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: .06em; font-size: 8.2pt; color: var(--tenue); text-align: left; padding: 0 2mm 1.5mm; border-bottom: 2px solid var(--verde); }
.tab td { padding: 2.4mm 2mm; border-bottom: 1px solid #e3e8e5; vertical-align: top; }
.tab td.n { font-family: Oswald, sans-serif; font-size: 16pt; color: var(--oro); width: 9mm; line-height: 1; }
.tab td.m { font-family: Oswald, sans-serif; color: var(--verde); font-size: 11.5pt; }
.nota { font-size: 8.8pt; color: var(--tenue); margin-top: 2mm; line-height: 1.45; }
.ob { font-size: 10pt; margin: 0 0 2.5mm; }
.ob b { color: var(--verde); }
.fase-chip { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm; margin-bottom: 3mm; }
.fase-chip div { background: var(--fondo); border-radius: 1.5mm; padding: 2mm 3mm; font-size: 8.8pt; line-height: 1.4; }
.fase-chip div b { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-weight: 500; letter-spacing: .05em; display: block; font-size: 8.5pt; }
.tempi { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; margin-top: 3mm; }
.tempi .box { padding: 3mm 4mm; font-size: 9pt; }
.tempi .box li { margin-bottom: 1mm; }
.attivi { display: flex; gap: 1.5mm; margin-top: 2mm; align-items: center; font-size: 8pt; color: var(--tenue); }
.attivi span { width: 7mm; height: 7mm; border-radius: 1.2mm; display: inline-flex; align-items: center; justify-content: center; font-family: Oswald, sans-serif; font-size: 12pt; background: var(--verde); color: var(--oro); }
.attivi span.off { background: #eef1ee; color: #c3ccc7; text-decoration: line-through; }
.tre { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; margin-top: 3mm; }
.tre .box { padding: 3mm 3.5mm; font-size: 8.6pt; line-height: 1.4; }
.tre .box h4 { font-size: 9.8pt; }
.tre .box li { margin-bottom: 1mm; }
.vignette { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }
.vignette .cap { font-family: Oswald, sans-serif; text-transform: uppercase; font-size: 8.5pt; color: var(--verde); letter-spacing: .05em; text-align: center; margin-top: 1mm; }
.osserva { margin-top: 3mm; font-size: 8.8pt; color: var(--testo); background: #fbf6e6; border-left: 4px solid var(--oro); padding: 2mm 3.5mm; border-radius: 0 1.5mm 1.5mm 0; }
.osserva b { font-family: Oswald, sans-serif; text-transform: uppercase; color: #9a7410; font-weight: 500; letter-spacing: .06em; }
.scheda td { height: 12mm; }
.riga { border-bottom: 1px solid #9aa7a1; display: inline-block; min-width: 40mm; }
.legenda { display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 6mm; margin-top: 2mm; font-size: 9.4pt; }
.legenda div { display: flex; align-items: center; gap: 3mm; }
</style>
</head>""", 1)

PAG = [0]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>DAI QUADERNI DEL MISTER</b><span>{PIEDE}</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo):
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>'


def freccia(d, tipo="passaggio"):
    """passaggio: bianco tratteggiato · movimento: oro · tiro: bianco pieno spesso."""
    if tipo == "movimento":
        return f'<path d="{d}" stroke="#f2c230" stroke-width="2.5" fill="none" marker-end="url(#freccia-oro)"/>'
    if tipo == "tiro":
        return f'<path d="{d}" stroke="#ffffff" stroke-width="4.5" fill="none" marker-end="url(#freccia)"/>'
    return f'<path d="{d}" stroke="#fff" stroke-width="2.5" fill="none" stroke-dasharray="7 5" marker-end="url(#freccia)"/>'


def testo(x, y, t, col="#f2c230", size=12, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="Oswald" font-size="{size}" font-weight="700" fill="{col}" '
            f'text-anchor="{anchor}" letter-spacing="1">{t}</text>')


def badge(x, y, t):
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="#0f3d2e" stroke="#f2c230" stroke-width="2"/>'
            + testo(x, y + 6, t, size=16))


def no(x, y):
    return (f'<g stroke="#ff4d3d" stroke-width="4" stroke-linecap="round">'
            f'<line x1="{x-8}" y1="{y-8}" x2="{x+8}" y2="{y+8}"/><line x1="{x+8}" y1="{y-8}" x2="{x-8}" y2="{y+8}"/></g>')


# Campo 7 contro 7 (40 × 30 m) disegnato in orizzontale: i rossi attaccano verso destra.
# 7 giocatori di movimento per squadra + 2 portieri bersaglio.
ROSSI = [(95, 105), (95, 275), (165, 190), (235, 110), (235, 270), (330, 150), (370, 245)]
BLU = [(425, 120), (425, 260), (360, 190), (285, 115), (285, 265), (205, 190), (130, 190)]


def campo(contenuto, rossi=ROSSI, blu=BLU, larghezza="118mm", etichette=True):
    gioc = "".join(g(x, y, "pA") for x, y in rossi) + "".join(g(x, y, "pB") for x, y in blu)
    et = (testo(145, 372, "METÀ DIFENSIVA DEI ROSSI", "#ffffff", 10)
          + testo(355, 372, "METÀ OFFENSIVA DEI ROSSI", "#ffffff", 10)) if etichette else ""
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:{larghezza};margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="25" width="440" height="330"/>
      <line x1="250" y1="25" x2="250" y2="355"/><circle cx="250" cy="190" r="32"/>
    </g>
    <g fill="none" stroke="#fff" stroke-width="3"><rect x="12" y="160" width="18" height="60"/><rect x="470" y="160" width="18" height="60"/></g>
    {g(21, 190, "pP")}{g(479, 190, "pP")}
    {et}
    {gioc}
    {contenuto}
  </svg>'''


def attivi(validi):
    return '<div class="attivi">Punti attivi ' + "".join(
        f'<span class="{"" if p in validi else "off"}">{p}</span>' for p in (1, 2, 3)) + "</div>"


def lista(voci):
    return "<ul class=\"clean\">" + "".join(f"<li>{v}</li>" for v in voci) + "</ul>"


def tappa(n, titolo, obiettivo, fasi, schema, t1, p1, t2, p2, attenzione, errori, osservare):
    fasi_html = "".join(f"<div><b>{k}</b>{v}</div>" for k, v in fasi)
    cols = "1fr 1fr" if len(fasi) == 2 else "1fr"
    return f'''<section class="page">
  <div class="kicker">Tappa {n} di 7</div>
  <div class="ex-title"><h2 style="font-size:20pt">{titolo}</h2></div>
  <p class="ob" style="margin-top:2mm"><b>Obiettivo principale:</b> {obiettivo}</p>
  <div class="fase-chip" style="grid-template-columns:{cols}">{fasi_html}</div>
  {schema}
  <div class="tempi">
    <div class="box"><h4>1° tempo · 8'</h4>{lista(t1)}{attivi(p1)}</div>
    <div class="box"><h4>2° tempo · 8'</h4>{lista(t2)}{attivi(p2)}</div>
  </div>
  <div class="tre" style="grid-template-columns:1.25fr 1fr">
    <div class="box"><h4>Punti di attenzione del mister</h4>{lista(attenzione)}</div>
    <div class="box"><h4>Errori da evitare</h4>{lista(errori)}</div>
  </div>
  <div class="osserva"><b>Osservare</b> · {osservare}</div>
  {footer()}
</section>'''


# ======================================================================
# COPERTINA
campo_cop = '''<svg class="campo" viewBox="0 0 500 300">
  <g fill="none" stroke="#24493a" stroke-width="2"><rect x="20" y="20" width="460" height="260"/>
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
    <div class="kick">Il calcio a modo mio · Dai quaderni del mister · Percorso 1</div>
    <h1>La ricerca<span>del portiere</span></h1>
    <div class="claim">Un bersaglio insolito. Decisioni sempre più vicine alla partita.</div>
    <p class="sub"><b>7 tappe progressive</b> per allenare qualità dell'ultimo passaggio, pressione sul portatore, compattezza e lettura della profondità.</p>
    <p class="sub">Normalmente non si cerca il gol: si cerca il portiere avversario. Ma una riconquista nella metà offensiva autorizza a concludere a rete. La squadra deve capire quando costruire, quando lanciare e quando pressare per guadagnarsi la possibilità di segnare.</p>
  </div>
</section>'''

# ======================================================================
# GUIDA AL PERCORSO (2 pagine)
guida1 = f'''<section class="page">
  <div class="kicker">Guida al percorso</div>
  <div class="ex-title"><h2>Che cosa allena davvero questa partita a tema</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>La <b>ricerca del portiere</b> è una partita direzionale nella quale l'obiettivo ordinario è un passaggio volontario, preciso e controllabile al <b>portiere bersaglio</b> avversario. C'è una sola eccezione fondamentale: se una squadra recupera il possesso nella metà campo offensiva, può concludere a rete e ottenere 2 punti segnando un gol vero.</p>
    <p>Il bersaglio orienta le scelte della squadra in possesso. La minaccia del passaggio diretto dalla propria metà campo costringe chi difende a leggere il tempo con cui l'avversario può giocare in profondità.</p>
    <p>Il valore non sta nel "correre di più", ma nel saper prendere <b>decisioni collettive</b> prima che l'azione sia già conclusa. Per chi ha palla il problema è creare e scegliere una linea di passaggio utile, con l'ultimo gesto eseguito con precisione. Per chi non ce l'ha è capire se il portatore ha tempo e postura per giocare in avanti, pressarlo per ridurne le possibilità e coordinare il movimento della linea difensiva.</p>
  </div>
  <div class="principio"><b>Principio da ripetere nelle correzioni</b>La palla coperta e la palla scoperta non sono etichette fisse, ma condizioni che possono cambiare in un istante. La linea difensiva reagisce anche alla posizione degli attaccanti e alla copertura dei compagni, non soltanto al pallone.</div>
  <h3 style="margin-top:6mm">Come leggere gli schemi</h3>
  <div class="legenda">
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#c8372d" stroke="#fff" stroke-width="2"/></svg> Rossi: attaccano verso destra</div>
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#2a5db0" stroke="#fff" stroke-width="2"/></svg> Blu: attaccano verso sinistra</div>
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#f2c230" stroke="#1d2421" stroke-width="2"/></svg> Portiere bersaglio</div>
    <div><svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg> Movimento o pressione</div>
    <div><svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg> Passaggio</div>
    <div><svg width="40" height="14"><path d="M2,7 L30,7" stroke="#1d2421" stroke-width="4.5"/><path d="M28,1 L39,7 L28,13 Z" fill="#1d2421"/></svg> Tiro in porta</div>
  </div>
  {footer()}
</section>'''

guida2 = f'''<section class="page">
  <div class="kicker">Guida al percorso</div>
  <div class="ex-title"><h2>Obiettivi per fase di gioco</h2></div>
  <div class="fasi3">
    <div class="box"><h4>In possesso</h4>{lista([
        "Riconoscere posizione del bersaglio, compagni, avversari e linee di passaggio prima della ricezione.",
        "Ricevere con postura orientata alla giocata successiva e offrire appoggi e sostegni a distanze utili.",
        "Far avanzare il gioco quando c'è vantaggio; usare scarico, cambio d'angolo o circolazione quando la via diretta è chiusa.",
        "Eseguire con precisione l'ultimo passaggio, sia corto sia diretto dalla propria metà campo, senza confondere fretta e verticalità."])}</div>
    <div class="box"><h4>In non possesso</h4>{lista([
        "Riconoscere i segnali concreti di <b>palla scoperta</b>: portatore libero dalla pressione, testa alta, controllo orientato, tempo e spazio per calciare.",
        "Riconoscere i segnali concreti di <b>palla coperta</b>: pressione efficace sul portatore, controllo chiuso o postura che non consente facilmente la giocata lunga.",
        "Pressare con tempi e angoli adeguati per ridurre il tempo e chiudere la linea di passaggio al bersaglio, non soltanto correre verso il pallone.",
        "Coordinare prima linea di pressione, compagni in copertura e linea difensiva; accorciare quando la giocata profonda è realmente ostacolata, proteggere lo spazio alle spalle quando è possibile.",
        "Conservare distanze tra reparti utili a intercettare e ad aggredire una seconda palla."])}</div>
    <div class="box"><h4>Nelle transizioni</h4>{lista([
        "Dopo la perdita, capire se si può aggredire immediatamente o se è necessario riorganizzarsi.",
        "Dopo una riconquista nella metà campo offensiva, sfruttare la possibilità speciale di concludere a rete: riconoscere se tirare subito o preparare la conclusione mantenendo il possesso; se la giocata non è favorevole, resta utile la ricerca del portiere bersaglio."])}</div>
  </div>
  {footer()}
</section>'''

# ======================================================================
# ORGANIZZAZIONE (2 pagine)
org1 = f'''<section class="page">
  <div class="kicker">Organizzazione</div>
  <div class="ex-title"><h2>Le regole che non cambiano</h2></div>
  <h3 style="margin-top:4mm">Disposizione</h3>
  <div class="elenco">{lista([
      "Due squadre di movimento, un portiere bersaglio per ciascuna estremità del campo. Le squadre attaccano in direzioni opposte.",
      "Per realizzare 1 o 3 punti una squadra deve trovare il portiere collocato all'estremità avversaria, che riceve e controlla la giocata dentro la porta. Per realizzare 2 punti serve invece un gol vero dopo un recupero nella metà campo offensiva.",
      "Nella ricerca ordinaria del bersaglio il portiere è un riferimento di ricezione: il punto da 1 o da 3 richiede un passaggio controllabile, non un tiro respinto o una deviazione fortuita. Nel caso del recupero alto, invece, la squadra cerca un gol reale: il portiere si comporta da portiere, difende la porta e prova a parare.",
      "Se la palla esce, rimessa dal punto di uscita secondo la modalità concordata con il gruppo (consigliata la rimessa con i piedi, per la continuità).",
      "In caso di fallo si interrompe e si riprende con un calcio libero. Evitare contatti con il portiere bersaglio e con le strutture della porta."])}</div>
  <h3 style="margin-top:5mm">Il punteggio</h3>
  <div class="punto"><div class="v">1</div><div><h4>Ricerca riuscita</h4>Il portiere bersaglio viene servito con un passaggio valido nel normale sviluppo del possesso.</div></div>
  <div class="punto"><div class="v">2</div><div><h4>Riconquista alta e gol</h4>Una squadra riconquista il pallone nella metà campo offensiva: da quel momento può tirare nella porta avversaria. Se supera il portiere, che difende normalmente la porta, e segna un gol vero nell'azione nata dalla riconquista, ottiene 2 punti. La sola riconquista non vale punti. Se invece trova il portiere con un passaggio, vale 1 punto.</div></div>
  <div class="punto"><div class="v">3</div><div><h4>Passaggio diretto da lontano</h4>Un unico passaggio calciato dalla propria metà difensiva arriva direttamente al portiere bersaglio, che lo controlla regolarmente. Non basta indirizzare genericamente la palla verso la porta.</div></div>
  <p class="nota">I punti non si sommano: per ogni azione si assegna soltanto il valore più alto. In ogni tappa sono indicati i punteggi attivi; gli altri non valgono.</p>
  {footer()}
</section>'''

org2 = f'''<section class="page">
  <div class="kicker">Organizzazione</div>
  <div class="ex-title"><h2>Tocchi, campo e tempi</h2></div>
  <h3 style="margin-top:4mm">Tocchi, ruoli e jolly</h3>
  <div class="elenco">{lista([
      "Il vincolo dei tocchi è un massimo, non un obbligo di usare ogni tocco disponibile.",
      "Nessun obbligo costante di giocare solo in avanti e nessun divieto generale del passaggio orizzontale: un passaggio laterale o uno scarico possono preparare la verticalizzazione.",
      "Il jolly per il numero dispari è un adattamento facoltativo, non la condizione di riferimento: la superiorità in possesso cambia tempi e difficoltà del pressing. Se possibile, usare le rotazioni per giocare in parità numerica.",
      "Dal 9 contro 9 in su si può usare il fuorigioco, se ci sono spazio e controllo arbitrale, spiegandolo prima ai giocatori."])}</div>
  <h3 style="margin-top:5mm">Misure consigliate dei campi</h3>
  <table class="tab">
    <tr><th>Giocatori di movimento</th><th>Lunghezza × larghezza</th><th>Spazio per giocatore</th></tr>
    <tr><td class="m">7 contro 7</td><td><b>40 × 30 m</b></td><td>circa 86 m²</td></tr>
    <tr><td class="m">8 contro 8</td><td><b>44 × 32 m</b></td><td>circa 88 m²</td></tr>
    <tr><td class="m">9 contro 9</td><td><b>48 × 36 m</b></td><td>circa 96 m²</td></tr>
    <tr><td class="m">10 contro 10</td><td><b>54 × 40 m</b></td><td>circa 108 m²</td></tr>
    <tr><td class="m">11 contro 11</td><td><b>60 × 46 m</b></td><td>circa 125 m²</td></tr>
  </table>
  <p class="nota">Sono un punto di partenza da provare in campo, non misure obbligatorie. La lunghezza deve restare sufficiente perché esista una vera profondità da proteggere e il passaggio da 3 punti resti praticabile. Se il bersaglio viene trovato da lontano troppo facilmente, allungare il campo di 5 m lasciando invariata la larghezza; se non ci sono possibilità credibili di pressing, stringerlo di 3-5 m; se tutto si risolve in mischie e non si distingue la palla scoperta, allargarlo leggermente. Adattare a età, categoria, livello tecnico, numero di giocatori e dimensione delle porte.</p>
  <h3 style="margin-top:5mm">Tempi del percorso</h3>
  <div class="elenco">{lista([
      "Ogni tappa: <b>1° tempo di 8' e 2° tempo di 8'</b>, con 1-2 minuti di confronto tra i tempi, rotazione dei ruoli o cambio campo quando serve.",
      "Le sette tappe non sono un'unica seduta: servono almeno 112 minuti di gioco effettivo, da distribuire in più allenamenti. Esempio: seduta A tappe 1-2, seduta B tappe 3-5, seduta C tappe 6-7.",
      "Nelle tappe 2 e 7 alcuni vincoli restano uguali tra i due tempi: la progressione consiste nell'aumentare l'autonomia delle decisioni, non nel moltiplicare le regole."])}</div>
  {footer()}
</section>'''

# ======================================================================
# QUADRO SINOTTICO
SINOTTICO = [
    ("Vedere e trovare il bersaglio", "4 tocchi", "3 tocchi", "1"),
    ("Difendere la minaccia della profondità", "3 tocchi", "Stesse regole, meno indicazioni", "1 · 3"),
    ("Coordinare pressione e linea", "3 tocchi", "Riconquista alta: tiro in porta consentito, gol = 2", "1 · 3 → 1 · 2 · 3"),
    ("Pressare come squadra", "3 tocchi", "2 tocchi nella metà offensiva", "1 · 2 · 3"),
    ("Creare una via corta quando quella diretta è tolta", "Niente diretto dalla metà difensiva al bersaglio, 3 tocchi", "Uguale + 2 tocchi nella metà offensiva", "1 · 2"),
    ("Scegliere tra diretto e costruzione sotto pressione", "3 tocchi, tornano tutte le soluzioni", "Stesse regole, scelta autonoma", "1 · 2 · 3"),
    ("Trasferire i principi in partita", "Tocchi liberi", "Tocchi liberi, gara", "1 · 2 · 3"),
]
righe = "".join(f'<tr><td class="n">{i}</td><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td style="font-family:Oswald;color:var(--verde);white-space:nowrap">{d}</td></tr>'
                for i, (a, b, c, d) in enumerate(SINOTTICO, 1))
sinottico = f'''<section class="page">
  <div class="kicker">La progressione</div>
  <div class="ex-title"><h2>Il quadro delle 7 tappe</h2></div>
  <table class="tab" style="margin-top:5mm">
    <tr><th></th><th>Problema di gioco</th><th>1° tempo</th><th>2° tempo</th><th>Punti</th></tr>
    {righe}
  </table>
  <div class="principio" style="margin-top:6mm"><b>Lettura della progressione</b>La tappa 1 sviluppa orientamento e precisione; la 2 introduce il rischio della profondità; la 3 collega pressione e linea; la 4 coordina il pressing e le transizioni; la 5 isola per un breve periodo la costruzione corta, riducendo dichiaratamente il rischio profondo; la 6 riunisce tutte le alternative; la 7 verifica il comportamento senza istruzioni continue. La difficoltà cresce nelle decisioni e nel lavoro collettivo, non nella somma dei divieti.</div>
  {footer()}
</section>'''

# ======================================================================
# LE 7 TAPPE
t1 = tappa(1, "Il bersaglio non è la porta",
    "vedere il portiere bersaglio e preparare una ricezione e un passaggio che consentano di trovarlo con precisione.",
    [("In possesso", "Scansione prima del controllo, postura aperta, sostegno vicino e soluzione in avanti, scelta dell'ultimo passaggio."),
     ("In non possesso", "Riconoscere e chiudere la linea di passaggio più immediata, senza inseguire sempre il pallone.")],
    campo(freccia("M165,178 L228,120") + freccia("M240,118 L322,146") + freccia("M342,154 L466,188")
          + freccia("M170,200 L274,258") + no(232, 234)
          + '<use href="#palla" x="176" y="198"/>' + testo(420, 170, "1 PUNTO")),
    ["Massimo <b>4 tocchi</b>", "Vale solo il portiere trovato con ricezione controllata", "Nessun bonus per lancio lungo o riconquista alta"], [1],
    ["Massimo <b>3 tocchi</b>", "Punteggio invariato", "Non chiedere di verticalizzare sempre: cercare prima il momento corretto"], [1],
    ["Il ricevente ha guardato portiere e avversari prima di ricevere?", "La squadra crea almeno due linee di passaggio utili al portatore?", "Il passaggio finale è calibrato sul bersaglio e non semplicemente calciato forte?"],
    ["Scambiare ogni tocco in avanti per una scelta giusta", "Chiedere di forzare il passaggio quando la linea è chiusa", "Correggere tutto insieme: qui conta capire bersaglio e appoggi"],
    "passaggi validi al portiere sul numero di tentativi; ricezioni orientate verso una soluzione utile.")

t2 = tappa(2, "Quando la profondità diventa una minaccia",
    "riconoscere quando il portatore può calciare lungo e adeguare in tempo la posizione della linea difensiva.",
    [("In possesso", "Vedere il passaggio diretto dalla propria metà campo solo quando ci sono spazio e qualità di esecuzione."),
     ("In non possesso", "Riconoscere la palla scoperta, attaccare il portatore per togliergli tempo, proteggere lo spazio alle spalle senza abbassarsi a ogni tocco.")],
    campo(freccia("M108,268 Q290,60 466,184") + '<use href="#palla" x="106" y="288"/>' + testo(290, 68, "DIRETTO DALLA METÀ DIFENSIVA · 3 PUNTI", size=11)
          + freccia("M205,205 L120,256", "movimento") + testo(165, 335, "PRESSIONE IN RITARDO", "#ffffff", 10)
          + freccia("M425,132 L452,150", "movimento") + freccia("M425,248 L452,226", "movimento") + freccia("M360,198 L392,210", "movimento")),
    ["Massimo <b>3 tocchi</b>", "Valgono la ricerca normale e il passaggio diretto dalla metà difensiva al bersaglio"], [1, 3],
    ["Stesse regole e stessi punti", "Meno indicazioni dalla panchina: il portatore riconosce da sé l'occasione, la difesa riconosce la minaccia"], [1, 3],
    ["Pressione effettiva sul portatore prima che prepari il calcio lungo", "Prima risposta della linea alla postura e al tempo del portatore, non solo alla traiettoria", "Coperture sul passaggio e posizione dei difendenti lontani dalla palla"],
    ["Dire «palla scoperta = scappa» senza guardare chi attacca lo spazio e quale copertura c'è", "Premiare ogni lancio tentato: i 3 punti chiedono un passaggio riuscito", "Confondere il passaggio al portiere con un rinvio senza destinatario"],
    "quante minacce di lancio vengono contrastate prima della partenza; quanti passaggi da 3 punti riescono.")

def mini(contenuto, didascalia):
    return f'<div>{campo(contenuto, larghezza="100%", etichette=False)}<div class="cap">{didascalia}</div></div>'

PRESSATO = freccia("M205,205 L180,260", "movimento") + freccia("M130,200 L118,255", "movimento")
t3 = tappa(3, "Coprire la palla, guidare la linea",
    "collegare il comportamento del primo difendente alla decisione del reparto arretrato di accorciare o proteggere la profondità.",
    [("In non possesso", "Il primo difendente chiude tempo e angolo della giocata lunga; chi è dietro legge l'efficacia della pressione e aggiorna le distanze."),
     ("In transizione positiva", "Sfruttare la riconquista alta per tirare e segnare, riconoscendo tempi e soluzioni di conclusione.")],
    '<div class="vignette">' + mini(PRESSATO + '<use href="#palla" x="106" y="288"/>'
                                    + freccia("M425,132 L392,132", "movimento") + freccia("M425,248 L392,248", "movimento") + freccia("M360,198 L330,198", "movimento"),
                                    "Portatore pressato · la linea accorcia")
    + mini('<use href="#palla" x="106" y="288"/>' + freccia("M425,132 L455,148", "movimento") + freccia("M425,248 L455,232", "movimento") + freccia("M360,198 L395,198", "movimento"),
           "Portatore libero · la linea protegge la profondità") + '</div>',
    ["Massimo <b>3 tocchi</b>", "Punti attivi come nella tappa 2", "Focus: tempi di pressione, copertura e linea, senza nuovi premi"], [1, 3],
    ["Massimo <b>3 tocchi</b>", "Si aggiunge il 2: dopo una riconquista nella metà offensiva si può tirare in porta; 2 punti solo se è gol"], [1, 2, 3],
    ["Il primo difendente orienta l'avversario verso una soluzione meno pericolosa?", "Il reparto arretrato distingue un pressing reale da una corsa verso la palla che non limita il passaggio?", "Dopo la riconquista alta, chi prepara il tiro e chi offre un sostegno utile senza rallentare?"],
    ["Accorciare mentre il portatore è libero di calciare", "Abbassarsi automaticamente anche se il portatore è stato coperto", "Pressare da soli senza coperture"],
    "prima reazione coordinata tra difendente vicino e linea; recuperi alti, conclusioni nate da questi recuperi e gol segnati.")

TIRO = (freccia("M300,232 L346,200", "movimento") + '<use href="#palla" x="372" y="232"/>'
        + freccia("M380,236 L466,200", "tiro") + testo(400, 290, "RICONQUISTA E TIRO · GOL = 2"))
t4 = tappa(4, "Pressare insieme, non uno alla volta",
    "coordinare la pressione del reparto avanzato, le coperture del centrocampo e la posizione della linea difensiva per produrre riconquiste utili.",
    [("In non possesso", "Angoli e tempi della pressione, chiusura della via centrale verso il bersaglio, squadra corta quando il contesto lo permette."),
     ("In transizione", "Riconquista nella metà offensiva, attacco immediato della porta, scelta tra tiro e passaggio che prepara il tiro.")],
    '<div class="vignette">' + mini(freccia("M330,162 L368,232", "movimento") + freccia("M370,258 L380,240", "movimento")
                                    + freccia("M235,250 L265,252", "movimento") + freccia("M130,190 L165,192", "movimento")
                                    + '<use href="#palla" x="425" y="268"/>', "Prima pressione, copertura e linea corta")
    + mini(freccia("M330,162 L368,232", "movimento") + '<use href="#palla" x="380" y="250"/>' + freccia("M382,244 L466,198", "tiro"),
           "Riconquista nella metà offensiva e tiro in porta") + '</div>',
    ["Massimo <b>3 tocchi</b>", "Pressare senza separare i reparti, mantenendo la minaccia del lancio diretto"], [1, 2, 3],
    ["Massimo <b>3 tocchi</b> nella propria metà, <b>2 tocchi</b> nella metà offensiva", "Si allenano velocità degli appoggi e ultimo passaggio, senza vietare scarichi o passaggi laterali"], [1, 2, 3],
    ["La prima pressione chiude una possibilità e indirizza il gioco o è una corsa senza obiettivo?", "Il centrocampo sostiene la pressione togliendo le linee di passaggio intermedie?", "La linea difensiva segue la squadra senza regalare profondità?"],
    ["Correre tutti sul portatore dimenticando gli avversari liberi", "Ridurre i tocchi anche dove si vuole osservare un lancio ponderato", "Valutare solo la riconquista e non l'azione successiva"],
    "recuperi nella metà offensiva, quanti generano tiri e quanti diventano gol da 2 punti; pressioni con i reparti collegati.")

t5 = tappa(5, "Costruire quando la via diretta è chiusa",
    "non trasformare la verticalizzazione in un obbligo: usare appoggi, sostegni, cambi d'angolo e passaggi tra le linee per creare una nuova via verso il bersaglio.",
    [("Scelta didattica", "Per una sola tappa si toglie il passaggio diretto dalla propria metà difensiva al portiere bersaglio. Non si vietano tutti i lanci: si elimina solo la scorciatoia da 3 punti, per osservare lo sviluppo del possesso e la pressione su giocate più ravvicinate.")],
    campo(freccia("M108,268 Q290,90 466,184") + no(290, 140) + '<use href="#palla" x="106" y="288"/>'
          + freccia("M100,262 L102,122") + freccia("M108,110 L226,112") + freccia("M240,120 L322,148") + freccia("M342,156 L466,188")
          + testo(300, 64, "DIRETTO DALLA METÀ DIFENSIVA NON CONSENTITO", "#ffffff", 10)),
    ["Massimo <b>3 tocchi</b>", "Non si può servire direttamente il portiere dalla propria metà difensiva", "Il 3 è sospeso"], [1, 2],
    ["Stesso divieto del passaggio diretto", "Massimo <b>3 tocchi</b> nella propria metà, <b>2 tocchi</b> nella metà offensiva"], [1, 2],
    ["Il passaggio indietro o laterale prepara una soluzione nuova o rinvia solo il problema?", "Il compagno tra le linee si offre con un angolo di ricezione utilizzabile?", "Dopo una perdita, il difendente vicino e quelli in copertura reagiscono insieme?"],
    ["Vietare tutti i lanci senza definire il vincolo", "Vietare i passaggi orizzontali: toglierebbe soluzioni da allenare", "Credere che la linea sappia difendere il lancio solo perché qui accorcia facilmente"],
    "quante azioni arrivano al bersaglio dopo aver creato una nuova linea di passaggio; recuperi alti con pressione collettiva.")

t6 = tappa(6, "Leggere e scegliere sotto pressione",
    "riportare tutte le soluzioni e allenare la scelta tra gioco diretto, consolidamento e conclusione dopo una riconquista alta, con pressione e coperture attive.",
    [("In possesso", "Valutare se c'è tempo per il diretto, se conviene creare un nuovo angolo di passaggio o se una riconquista alta permette di tirare."),
     ("In non possesso", "Reagire ai continui cambi da palla coperta a scoperta e viceversa.")],
    '<div class="vignette">' + mini('<use href="#palla" x="106" y="288"/>' + freccia("M108,268 Q290,90 466,184")
                                    + freccia("M425,132 L455,148", "movimento") + freccia("M425,248 L455,232", "movimento"),
                                    "Portatore libero · diretto e linea che protegge")
    + mini(PRESSATO + '<use href="#palla" x="106" y="288"/>' + freccia("M100,262 L102,122")
           + freccia("M425,132 L392,132", "movimento") + freccia("M425,248 L392,248", "movimento"),
           "Portatore pressato · scarico e linea che accorcia") + '</div>',
    ["Massimo <b>3 tocchi</b>", "Torna valido il passaggio diretto dalla metà difensiva al bersaglio"], [1, 2, 3],
    ["Stesse regole e stessi punti", "Il mister non indica la soluzione: osserva se le squadre decidono da sole quando aggredire, proteggere, scaricare o giocare lungo"], [1, 2, 3],
    ["Che cosa ha visto il portatore prima della scelta?", "La squadra senza palla cambia altezza in base alla pressione effettiva?", "I compagni lontani dalla palla preparano appoggio, copertura o difesa della profondità?"],
    ["Premiare il 3 anche quando nasce da una scelta forzata", "Scambiare la velocità di esecuzione per una scelta migliore", "Suggerire ogni comportamento dalla panchina"],
    "qualità delle scelte senza correzione immediata; rapporto tra passaggi diretti tentati e riusciti.")

t7 = tappa(7, "La partita: senza la risposta del mister",
    "verificare se i comportamenti emergono in una partita senza indicazioni costanti e senza vincoli di tocchi.",
    [("Il mister", "Osserva senza chiamare continuamente «scappa» o «accorcia». Alla fine, breve confronto: su quali segnali ciascuna squadra ha basato le proprie decisioni?")],
    campo(freccia("M165,178 L228,120") + freccia("M240,118 L322,146") + freccia("M342,154 L466,186") + badge(405, 200, "1")
          + freccia("M108,268 Q300,40 466,180") + badge(290, 52, "3")
          + freccia("M300,232 L346,250", "movimento") + freccia("M375,262 L466,204", "tiro") + '<use href="#palla" x="368" y="264"/>' + badge(440, 270, "2") + testo(440, 305, "TIRO, IL PORTIERE PARA", "#ffffff", 9)
          + '<use href="#palla" x="176" y="198"/>'),
    ["<b>Tocchi liberi</b>", "Tutte le soluzioni consentite"], [1, 2, 3],
    ["Stesse regole, punteggi e libertà", "Cambio campo e gara a punteggio"], [1, 2, 3],
    ["La prima pressione cambia davvero la possibilità di lancio dell'avversario?", "La linea riconosce da sola quando proteggere le spalle e quando avanzare?", "Il passaggio diretto si usa con precisione quando c'è, senza cercarlo a ogni possesso?", "La squadra pressa alta senza disunirsi se non riconquista?"],
    ["Tornare a un numero fisso di tocchi", "Usare il punteggio come unico criterio di successo", "Correggere ogni decisione dall'esterno"],
    "esempi spontanei di pressione efficace, risposta della linea e scelta del passaggio; confronto con le tappe 1 e 2.")

# ======================================================================
# SCHEDA DI OSSERVAZIONE
INDICATORI = ["Passaggi al portiere riusciti / tentati", "Passaggi diretti da 3 punti riusciti / tentati",
              "Pressioni efficaci prima del possibile lancio", "Riconquiste nella metà offensiva",
              "Gol segnati dopo riconquista alta (2 punti)", "Linea che accorcia o protegge con il tempo giusto"]
r_ind = "".join(f"<tr><td>{i}</td><td></td><td></td><td></td></tr>" for i in INDICATORI)
scheda = f'''<section class="page">
  <div class="kicker">Strumento di lavoro</div>
  <div class="ex-title"><h2>Scheda di osservazione</h2></div>
  <p class="ob" style="margin-top:4mm">Squadra <span class="riga"></span> &nbsp; Categoria <span class="riga" style="min-width:30mm"></span></p>
  <p class="ob">Data <span class="riga" style="min-width:30mm"></span> &nbsp; Tappa <span class="riga" style="min-width:15mm"></span> &nbsp; Formato e campo <span class="riga"></span></p>
  <table class="tab scheda" style="margin-top:4mm">
    <tr><th style="width:45%">Indicatore osservabile</th><th>Prima parte</th><th>Parte finale</th><th>Nota del mister</th></tr>
    {r_ind}
  </table>
  <p class="ob" style="margin-top:7mm"><b>Una correzione prioritaria per il prossimo allenamento</b></p>
  <div style="border-bottom:1px solid #9aa7a1;height:9mm"></div><div style="border-bottom:1px solid #9aa7a1;height:9mm"></div>
  <p class="nota" style="margin-top:5mm">Annotazioni semplici e brevi: la scheda serve a guardare meglio, non a trasformare il mister in uno statistico durante il gioco. I numeri raccolti aiutano a orientare il lavoro; non dimostrano da soli un miglioramento nelle partite ufficiali.</p>
  {footer()}
</section>'''

pagine = [copertina, guida1, guida2, org1, org2, sinottico, t1, t2, t3, t4, t5, t6, t7, scheda]
html = testa + "\n\n".join(pagine) + "\n\n</body>\n</html>\n"
(QUI / "percorso-ricerca-del-portiere.html").write_text(html)
print("pagine:", len(pagine))
