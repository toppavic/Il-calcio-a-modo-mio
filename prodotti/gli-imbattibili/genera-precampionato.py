"""Genera precampionato-allenamenti-1-10.html: il pacchetto "Il precampionato" con gli Allenamenti 1-10.

Revisione del 26/10/2026, stesso standard del volume "In campionato": una sola copertina, per ogni allenamento
la pagina con le foto del foglio originale (data, precisazioni dell'autore, adattamenti consigliati), le pagine
dell'allenamento e una pagina di indicazioni tecniche dopo ogni esercitazione principale. Numerazione continua
e indice calcolato sulle pagine vere. Contenuti editoriali in precampionato_editoriale.py.
Uso: prima gli script genera-allenamento-02…10.py (l'1 è già HTML), poi python3 genera-precampionato.py e render.js
"""
import pathlib
import re

from precampionato_editoriale import FONTI, TECNICHE

QUI = pathlib.Path(__file__).parent
N = range(1, 11)
html = {i: (QUI / f"allenamento-{i:02d}.html").read_text() for i in N}
SEZ = re.compile(r'<section class="page[^"]*">.*?</section>', re.S)

# Stili e simboli SVG: l'Allenamento 10 contiene quelli di tutti gli altri
testa = html[10][: html[10].index("<!-- 1. COPERTINA -->")]
testa = re.sub(r"<title>.*?</title>", "<title>Gli Imbattibili – Il precampionato, Allenamenti 1-10</title>", testa)
testa = testa.replace("</style>\n</head>", """
.indice { width: 100%; border-collapse: collapse; margin-top: 4mm; }
.indice td { padding: 3mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10.5pt; vertical-align: middle; }
.indice .n { font-family: Oswald, sans-serif; font-size: 20pt; color: var(--oro); width: 14mm; }
.indice .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 13pt; letter-spacing: .02em; }
.indice .d { color: #5d6b65; font-size: 9.8pt; }
.indice .p { font-family: Oswald, sans-serif; color: var(--verde); font-size: 13pt; text-align: right; width: 16mm; }
.legenda { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 6mm; margin-top: 3mm; font-size: 10pt; }
.legenda div { display: flex; align-items: center; gap: 3mm; }
.legenda svg { flex: none; }
.testo p { font-size: 11pt; line-height: 1.6; margin-bottom: 3mm; }
/* leggibilità su smartphone: riquadri su una riga ciascuno, testo più grande */
.three { grid-template-columns: 1fr !important; gap: 2mm !important; margin-top: 4mm !important; }
.three .box { display: grid; grid-template-columns: 33mm 1fr; gap: 4mm; font-size: 10pt !important; padding: 2.6mm 4mm; }
.three .box h4 { margin: 0; font-size: 10.5pt; }
.three .box p { margin-bottom: 1mm !important; }
.three .box p:last-child { margin-bottom: 0 !important; }
.three .box ul.clean li { margin-bottom: .6mm; }
.chip { font-size: 8.8pt !important; }
.obj { font-size: 10.5pt; }
/* livelli delle fonti */
.liv { display: inline-block; font-family: Oswald, sans-serif; font-size: 8.5pt; letter-spacing: .08em; text-transform: uppercase; padding: .6mm 2.4mm; border-radius: 1mm; margin-right: 2mm; vertical-align: 1px; }
.liv.q { background: var(--verde); color: #fff; }
.liv.a { background: var(--oro); color: var(--verde); }
.liv.c { background: #e6efe9; color: var(--verde); border: 1px solid #b9cdc2; }
.foglio { display: block; margin: 3mm auto 0; max-height: 150mm; max-width: 100%; border: 1px solid #dfe5e1; border-radius: 1.5mm; box-shadow: 0 1mm 3mm rgba(0,0,0,.08); }
.fonti { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 4mm; }
.fonti .box { font-size: 9.8pt; line-height: 1.45; padding: 3mm 4mm; }
.fonti .box li { margin-bottom: 1mm; }
.nota-f { margin-top: 3mm; font-size: 9.6pt; background: #fbf6e6; border-left: 4px solid var(--oro); padding: 2.2mm 3.5mm; border-radius: 0 1.5mm 1.5mm 0; }
.tec h3 { font-size: 11pt; margin: 4mm 0 1.5mm; }
.tec .riga { display: grid; grid-template-columns: 30mm 1fr; gap: 4mm; padding: 2.2mm 0; border-bottom: 1px solid #e3e8e5; font-size: 10.2pt; }
.tec .riga .l { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 10pt; letter-spacing: .04em; }
.tec .ob { font-size: 11pt; line-height: 1.55; margin: 3mm 0 2mm; }
.tec .liste { display: grid; grid-template-columns: 1fr; gap: 3mm; margin-top: 3mm; }
.tec .liste .box { font-size: 10.2pt; line-height: 1.45; padding: 3mm 4.5mm; }
.tec .liste .box li { margin-bottom: 1mm; }
.osserva { margin-top: 4mm; font-size: 9.8pt; background: #edf4ef; border-left: 4px solid var(--verde); padding: 2.5mm 4mm; border-radius: 0 1.5mm 1.5mm 0; }
.osserva h4 { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 10.5pt; letter-spacing: .04em; margin-bottom: 1mm; }
.osserva .nb { color: var(--tenue); font-size: 8.8pt; margin-top: 1mm; }

.stazioni-t { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm; font-size: 10pt; }
.stazioni-t td { padding: 2.2mm 3mm; border-bottom: 1px solid #e3e8e5; vertical-align: middle; }
.stazioni-t th { text-align: left; font-size: 7.5pt; text-transform: uppercase; letter-spacing: .1em; color: var(--tenue); padding: 0 3mm 2mm; font-weight: 600; border-bottom: 2px solid var(--verde); }
.stazioni-t .s { font-family: Oswald, sans-serif; font-size: 15pt; color: var(--oro); width: 12mm; }
.stazioni-t .vol { font-family: Oswald, sans-serif; color: var(--verde); white-space: nowrap; font-size: 11pt; }
.stazioni-t .cue { color: var(--tenue); font-size: 9pt; display: block; margin-top: .5mm; }
.fogli { display: flex; gap: 4mm; justify-content: center; align-items: flex-start; margin-top: 3mm; }
.fogli .foglio { margin: 0; max-height: 140mm; max-width: 49%; }
</style>
</head>""", 1)


def lista(voci):
    return '<ul class="clean">' + "".join(f"<li>{v}</li>" for v in voci) + "</ul>"


def piede(i):
    return f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento {i}</span><span>#</span></div>'


FISICO = ('<div class="nota-f"><b>Lavoro fisico</b> (circuiti, corsa, intermittenti, navette, rapidità, suicidi): è la documentazione di '
          "quanto svolto con questa squadra, non una prescrizione. Chi lo riusa lo adatta al proprio gruppo.</div>")


# ---------- Pagina del foglio originale (al posto della copertina di ogni allenamento)
def pagina_foglio(i):
    f = FONTI[i]
    data = f" · {f['data']}" if f["data"] else " · data non indicata sul foglio"
    foto = "".join(f'<img class="foglio" src="../../materiale/precampionato/{x}">' for x in f["foto"])
    foto = f'<div class="fogli">{foto}</div>' if len(f["foto"]) > 1 else foto
    return f'''<section class="page">
  <div class="kicker">{f["settimana"]}{data}</div>
  <div class="ex-title"><h2>Allenamento {i} · il foglio originale</h2></div>
  {foto}
  <div class="fonti">
    <div class="box"><h4><span class="liv a">Precisato dall'autore</span></h4>{lista(f["autore"])}</div>
    <div class="box"><h4><span class="liv c">Consigliato</span></h4>{lista(f["consigliato"])}</div>
  </div>
  {FISICO}
  {piede(i)}
</section>'''


# ---------- Pagina di indicazioni tecniche
def pagina_tecnica(i, t):
    return f'''<section class="page tec">
  <div class="kicker">Allenamento {i} · Indicazioni tecniche · <span style="color:var(--tenue)">aggiunta editoriale, non presente nel quaderno</span></div>
  <div class="ex-title"><h2>{t["titolo"]}</h2></div>
  <p class="ob"><span class="liv c">Consigliato</span><b>Obiettivo tecnico-tattico.</b> {t["obiettivo"]}</p>
  <div class="riga"><div class="l">Tempi</div><div>{t["tempi"]}</div></div>
  <div class="riga"><div class="l">Campo</div><div>{t["campo"]}</div></div>
  <div class="liste">
    <div class="box"><h4>Punti di attenzione del mister</h4>{lista(t["attenzione"])}</div>
    <div class="box"><h4>Errori da evitare</h4>{lista(t["errori"])}</div>
    <div class="box"><h4>Comportamenti osservabili</h4>{lista(t["osservabili"])}</div>
  </div>
  {piede(i)}
</section>'''


RIDUCI = {(1, 2): .85, (1, 3): .7, (1, 7): .88, (2, 2): .82, (3, 2): .75, (4, 2): .66, (6, 2): .95}


def pagine_allenamento(i):
    sez = SEZ.findall(html[i])
    out = [pagina_foglio(i)]
    for k, s in enumerate(sez[1:], 1):  # la copertina (sezione 0) è sostituita dalla pagina del foglio
        s = re.sub(r'(<div class="box"><h4>(?:Organizzazione|Svolgimento|Punti chiave)</h4>)(.*?)(</div>)',
                   r'\1<div>\2</div>\3', s, flags=re.S)
        if i == 1 and k == 3:  # tabella delle stazioni a tutta larghezza, schema più piccolo
            s = s.replace('<table class="stazioni">', '<table class="stazioni-t">')
        if (i, k) in RIDUCI:  # schema ridotto dove la pagina, con i riquadri su una riga, sfora
            s = re.sub(r'(<svg class="diagram"[^>]*?width:)(\d+)mm', lambda m: f"{m[1]}{int(int(m[2]) * RIDUCI[(i, k)])}mm", s, count=1)
        s = re.sub(r'(<div class="footer">.*?<span>)\d+(</span></div>)', r"\1#\2", s)
        out.append(s)
        if (i, k) in TECNICHE:
            out.append(pagina_tecnica(i, TECNICHE[(i, k)]))
    return out


# ---------- Copertina del pacchetto (immagine già pronta, sotto i 20 MB di Etsy)
copertina = ('<section class="page" style="padding:0"><img src="copertine-pacchetto/copertina-00.jpg" '
             'style="width:100%;height:100%;display:block"></section>')

FOOT = '<div class="footer"><b>GLI IMBATTIBILI</b><span>Il precampionato · Allenamenti 1-10</span><span>#</span></div>'


def pallino(colore, bordo="#fff", testo=""):
    t = f'<text x="13" y="17.5" font-family="Oswald" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">{testo}</text>' if testo else ""
    return f'<svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="{colore}" stroke="{bordo}" stroke-width="2"/>{t}</svg>'


freccia_oro = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg>'
passaggio = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg>'

intro = f'''<section class="page">
  <div class="kicker">Il precampionato</div>
  <div class="ex-title"><h2>Prima di cominciare</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Questi sono gli allenamenti veri del precampionato della <b>Juniores provinciale che ha poi vinto il campionato senza perdere una partita</b>, trascritti dai quaderni dell'allenatore seduta per seduta e nell'ordine in cui sono stati svolti, dal 30 agosto al 20 settembre 2021.</p>
    <p>La squadra gioca con il <b>4-2-3-1</b>. La linea difensiva, guardando lo schema con la porta in alto, è sempre <b>2-5-6-3</b> da sinistra a destra. Il lavoro sulla linea segue una progressione: scivolamenti, spaccare la linea, difesa sul lancio, «Ti lascio alle spalle», 6 contro 4, cross in diagonale invertita.</p>
    <p>Ogni allenamento comincia con la <b>foto del foglio originale</b>. Poi la scheda della seduta, una pagina per ogni esercitazione e, dopo ogni esercitazione principale, una pagina di <b>indicazioni tecniche</b>.</p>
  </div>
  <h3 style="margin-top:5mm">Tre livelli di informazione</h3>
  <div class="box" style="font-size:10.2pt;line-height:1.5">
    <p style="margin-bottom:2mm"><span class="liv q">Dal quaderno</span>Esercitazioni, regole, punteggi, tempi e misure scritti sul foglio. Le pagine degli allenamenti li riportano così come sono.</p>
    <p style="margin-bottom:2mm"><span class="liv a">Precisato dall'autore</span>Chiarimenti dati dall'allenatore nel 2026, dove il foglio era incompleto o ambiguo.</p>
    <p><span class="liv c">Consigliato</span>Misure in metri dove il foglio non le riporta, obiettivi, punti di attenzione, errori da evitare e comportamenti da osservare. Sono indicazioni editoriali, non annotazioni storiche.</p>
  </div>
  <div class="nota-f"><b>Lavoro fisico.</b> Circuiti, corsa con variazioni di velocità, intermittenti, navette, rapidità e suicidi sono riportati come sono stati svolti con questa squadra, senza aggiungere carichi o recuperi. Non sono una prescrizione valida per ogni gruppo: vanno adattati all'età, al livello e alla condizione dei propri giocatori. I <b>suicidi</b> sono navette dalla linea dell'area piccola alla linea dell'area di rigore e ritorno: 11 m + 11 m, 22 m per navetta.</div>
  {FOOT}
</section>'''

intro2 = f'''<section class="page">
  <div class="kicker">Il precampionato</div>
  <div class="ex-title"><h2>Come leggere gli schemi</h2></div>
  <div class="legenda" style="margin-top:5mm">
    <div>{pallino("#2a5db0", testo="5")} Difensori e squadra di riferimento (numerati)</div>
    <div>{pallino("#c8372d")} Attaccanti e avversari</div>
    <div>{pallino("#f2c230", "#1d2421")} Portiere</div>
    <div>{pallino("#ffffff", "#1d2421")} Jolly</div>
    <div>{freccia_oro} Movimento del giocatore</div>
    <div>{passaggio} Passaggio, lancio o cross</div>
  </div>
  <h3 style="margin-top:7mm">Tempi e misure</h3>
  <div class="testo">
    <p>Nei programmi delle sedute il tempo di ogni blocco è quello del quaderno. Nelle indicazioni tecniche trovi anche il <b>gioco effettivo</b> e i recuperi: dove un dato non è scritto sul foglio è indicato come <b>non documentato</b>, senza inventare pause o recuperi.</p>
    <p>Le misure scritte dall'allenatore («50 m × larghezza del campo», «3/4 di campo», «metà campo con area») restano come sono. Accanto trovi la misura in metri su un campo regolamentare da 105 × 68 m e, dove il foglio non dice nulla, una <b>misura consigliata</b>, sempre segnalata come tale.</p>
  </div>
  <div class="chiave" style="margin-top:7mm">
    <span class="kicker">Il libro</span>
    La stagione di questa squadra è raccontata nel libro <b>“Gli Imbattibili”</b>, su Amazon. Il libro racconta cosa è successo. Questi allenamenti mostrano come ci siamo arrivati.
  </div>
  {FOOT}
</section>'''


def campo_scheda(h, etichetta):
    m = re.search(rf'<div class="l">{etichetta}</div><div class="v">(.*?)</div>', h)
    return m.group(1) if m else ""


blocchi = {i: pagine_allenamento(i) for i in N}
inizio, p = {}, 5  # copertina, prima di cominciare, schemi, indice: il primo allenamento parte da p. 5
for i in N:
    inizio[i] = p
    p += len(blocchi[i])
totale = p - 1

righe = []
for i in N:
    durata, focus = campo_scheda(html[i], "Durata"), campo_scheda(html[i], "Focus")
    sett = FONTI[i]["settimana"].split("· ")[1].lower()
    righe.append(f'<tr><td class="n">{i}</td><td><div class="t">Allenamento {i} · {sett}</div>'
                 f'<div class="d">{focus} · {durata}</div></td><td class="p">p. {inizio[i]}</td></tr>')

indice = f'''<section class="page">
  <div class="kicker">Il precampionato</div>
  <div class="ex-title"><h2>Indice</h2></div>
  <table class="indice">{"".join(righe)}</table>
  {FOOT}
</section>'''

tutte = [copertina, intro, intro2, indice] + [s for i in N for s in blocchi[i]]
assert len(tutte) == totale
numerate = [s.replace("<span>#</span>", f"<span>{n}</span>") for n, s in enumerate(tutte, 1)]

out = testa + "\n\n".join(numerate) + "\n\n</body>\n</html>\n"
(QUI / "precampionato-allenamenti-1-10.html").write_text(out)
print("pagine:", totale, "· inizio allenamenti:", inizio)
