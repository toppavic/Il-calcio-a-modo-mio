# Il calcio a modo mio – guida del progetto

Progetto per vendere PDF di allenamento (prima su Etsy). Il materiale viene dagli appunti di
un allenatore che con la sua **Juniores provinciale ha vinto il campionato senza perdere una
partita**. La serie si chiama **"Gli Imbattibili"**. Oggi (stagione 2026/27) allena il **Vaglia in Seconda
Categoria** (Toscana).

## Come lavorare con l'allenatore

- Scrive in italiano, spesso dal telefono, a volte con messaggi vocali trascritti. Rispondere
  in italiano, con calma, un passo alla volta e senza elenchi lunghi di opzioni.
- **Non mettere la virgola prima di "e"**, salvo incisi o ripetizioni enfatiche.
- Manda **foto dei fogli scritti a mano** (o note dal telefono) di un allenamento alla volta.
- Flusso: trascrivere → impaginare il PDF → inviarlo → fare **poche domande precise** solo
  sui punti illeggibili o ambigui → correggere.
- **Mai inventare contenuti tecnici presentandoli come suoi.** Obiettivi e punti chiave scritti
  da noi vanno bene, ma va sempre detto all'allenatore cosa è stato aggiunto perché lo controlli.
- Salvare ogni foto ricevuta in `materiale/` e fare commit e push dopo ogni passo.
- L'allenatore usa **due conversazioni separate**: una per gli **allenamenti** (trascrizione e PDF) e una
  per il **marketing** (post, Etsy, agenda). Tenere ognuna sul suo tema e fare sempre `git pull` prima di lavorare.

## Struttura del repository

- `materiale/precampionato/` – foto originali (`allenamento-NN.jpg`, `allenamento-NN-b.jpg`…)
- `materiale/da-classificare/` – note non ancora assegnate a un allenamento
- `materiale/brand/` – logo "Il calcio a modo mio" (`logo-cerchio.png` già ritagliato) e figura intera
- `prodotti/gli-imbattibili/` – **un PDF per allenamento**: `allenamento-NN.html` + `.pdf`
- `prodotti/linea-difensiva/` – PDF tematico sulla linea difensiva (bozza, messo da parte)
- `prodotti/stili-grafici/` – prove di stile e copertine scartate (solo riferimento)
- `strumenti/render.js` – HTML → PDF A4 + anteprime PNG
- `prodotti/gli-imbattibili/precampionato-allenamenti-1-10.pdf` – **pacchetto in vendita** (64 pagine): `genera-precampionato.py`
  unisce i 10 allenamenti con copertina, "Prima di cominciare" e indice. Le copertine vanno prima rese immagini
  (`strumenti/render-copertine.js` → `copertine-pacchetto/*.jpg`) sennò il PDF pesa 26 MB (limite Etsy 20 MB).
- `marketing/etsy/` – annuncio Etsy: `annuncio.md` (titolo, descrizione, tag), `immagini/` (foto 2000×1500,
  da `immagini-annuncio.html` con `strumenti/render-etsy.js`)
- `marketing/reel/` – Reel animati: HTML con `draw(t)`, `strumenti/render-reel.js` lo registra in MP4 1080×1920
- `marketing/social/` – post social: `genera-post.py` crea i caroselli 4:5 (IG/FB) e 9:16 (TikTok),
  `strumenti/render-post.js` li salva in `immagini/`, testi e indicazioni in `testi-dei-post.md`

## Come si crea il PDF di un nuovo allenamento

Il modello da copiare è `prodotti/gli-imbattibili/genera-allenamento-02.py`: legge lo stile e i
simboli SVG da `allenamento-01.html` e costruisce le pagine con funzioni Python
(`pagina_esercizio`, `mezzo_campo`, `fase`, `g`, `freccia`). Per l'Allenamento N:

1. copiare lo script in `genera-allenamento-NN.py` e cambiare contenuti e foto di copertina;
2. `python3 genera-allenamento-NN.py`;
3. `NODE_PATH=$(npm root -g) node strumenti/render.js prodotti/gli-imbattibili/allenamento-NN.html <scratchpad>`;
4. guardare **tutte** le anteprime PNG (sovrapposizioni, testo che tocca il piè di pagina);
5. commit, push e invio del PDF all'allenatore.

Playwright e Chromium sono già installati nell'ambiente. I font sono locali
(`prodotti/gli-imbattibili/font/`), niente Google Fonts a runtime.

## Stile grafico (deciso dall'allenatore)

- **Copertina**: logo circolare in alto, sotto la foto del foglio dell'allenamento in bianco e
  nero scurito, titolo "GLI / IMBATTIBILI" in bianco e verde logo `#84b94a`, sottotitolo
  "Precampionato · Allenamento N". **Niente scritta "0 sconfitte"** (non gli piace). Niente data.
- **Pagine interne**: verde scuro `#0f3d2e` e oro `#d4a017`, titoli Oswald maiuscolo, testo Inter.
  L'allenatore ha detto di lasciarle così (non passare ai colori del logo).
- Pagina 2: scheda della seduta (durata, giocatori, campo, focus, programma, barra dei tempi).
- Ogni esercitazione: kicker, titolo, chip, **Obiettivo**, schema, poi tre riquadri
  **Organizzazione / Svolgimento / Punti chiave**. Esercizi in più tempi → schemi in sequenza
  (vedi "Ti lascio alle spalle" nell'Allenamento 2).
- Schemi: campo verde a strisce, attaccanti rossi, difensori blu numerati, portiere giallo,
  jolly bianchi, movimenti in oro, passaggi/lanci tratteggiati bianchi.

## Convenzioni tecniche dell'allenatore

- Sistema di gioco sempre **4-2-3-1**: difensori 2-5-6-3, mediani 4 e 8, esterni 7 (a sinistra
  guardando lo schema con la porta in alto) e 11, trequartista 10, punta 9. Negli schemi con squadre
  intere disporre i giocatori così; se sono 9 si toglie il trequartista (4 + 2 mediani + 2 esterni + punta).
  Vale dall'Allenamento 6 in poi: gli schemi degli Allenamenti 1-5 restano come sono (deciso dall'allenatore).
- Linea difensiva sempre **2-5-6-3** da sinistra a destra guardando lo schema (porta in alto).
- Nei fogli: X = attaccanti, O = difensori, P = portiere. "Lo faccio io" = esercizio condotto
  dall'allenatore.
- Lavoro a gruppi: il gruppo si divide in due e **si invertono** (15' per gruppo).
- "Ricerca del portiere": ogni squadra attacca verso un portiere che fa da bersaglio.
- "Solo verticale": passaggi in avanti, all'indietro o in diagonale, mai orizzontali.
- Difesa sul cross: "diagonale invertita" (il terzino lato palla è il più vicino alla linea di fondo, gli altri salgono man mano). Terzino lato palla leggermente sotto la linea della palla, centrali e terzino
  opposto in leggera diagonale, centrocampisti a cerniera (il più vicino tra terzino e centrale, l'altro tra i centrali).
- Gioco di posizione: 4 contro 4 + 2 jolly (9 e 10), 15 passaggi consecutivi = 1 punto.

## Stato

- Allenamento 1 ✅ completo e confermato.
- Allenamento 2 ✅ completo; in attesa di conferma sulla nuova versione di "Ti lascio alle spalle".
- Allenamento 3 ✅ completo e confermato (125'; gioco di posizione 30 × 30 m, 15 passaggi = 1 punto).
- Allenamento 4 ✅ completo (95' + suicidi; marcature preventive; 3' di recupero tra i blocchi atletici). Cross in diagonale invertita confermato.
- Allenamento 5 ✅ completo e confermato (113'; uscite della difesa sul centrocampo a partita, 4 serie da 4' tutte a punti con 2' di recupero).
- Allenamento 6 ✅ completo e confermato (100'; pressione a squadra corta, gol normale 1 punto; nell'attacco contro difesa X difende e O attacca).
- Allenamento 7 ✅ completo e confermato (100'; vincolo di reparto solo nel 1° tempo, scaletta 8 volte). Punizioni difensive: l'allenatore non spiega il suo metodo, ognuno le gestisce come crede.
- Allenamento 8 ✅ completo e confermato (circa 110'; emergenza: O difende, XL attaccanti avversari; "30 m" sul foglio = 30 minuti).
- Allenamento 9 ✅ completo e confermato (90-95'; gol normale 1 punto; angoli difensivi come le punizioni, ognuno li organizza come crede).
- Allenamento 10 ✅ completo e confermato (85' + suicidi; corsia solo per il cross in entrambi i tempi).
- Allenamento 11 ✅ seconda versione (75' + suicidi; rapidità 4 stazioni × 8; 4c4 con 4 sponde 20×20, 5 serie da 5',
  gol valido solo di prima su passaggio della sponda; poi partita libera 2 × 10'). Sul foglio c'è scritto "1 ora":
  chiesto se tenere 75'. Disposizione delle sponde ancora da confermare.
- ✅ Pacchetto "Il Precampionato" (Allenamenti 1-10) **pubblicato su Etsy** il 2/10/2026: prezzo annuncio 8,11 € + IVA 22% aggiunta da Etsy = 9,89 € per chi compra dall'Italia (digitale, quantità 999,
  rinnovo automatico, dichiarato "con un generatore di IA", tag inseriti). Titolo con "i primi 10 allenamenti".
  Bio Instagram: link "Gli Imbattibili, gli allenamenti" (annuncio Etsy) sotto quello del libro, fatto il 2/10.
  Niente post di vendita subito (proposta, l'allenatore era d'accordo a non postare subito). Poi una riga
  "le sedute complete sono nel link in bio" nelle didascalie dei prossimi post, lancio vero dopo 2-3 post di valore
  con Allenamento 1 gratis ("commenta PRECAMPIONATO"). Prossimo: Allenamento 11.
- Marketing: Etsy da solo non porta clienti (già provato senza vendite). Strategia: post gratuiti
  sui social (gruppi Facebook di allenatori, Instagram, TikTok) con la storia della Juniores imbattuta,
  link a Etsy solo nel profilo. Primi 3 post pronti (cross, partita preventiva, gioco di posizione).
  Account: Instagram "Il calcio a modo mio", TikTok "Matteo Falleri", Facebook = profilo personale
  usato come diario (niente pagina): nei gruppi Facebook pubblica con il profilo personale.
  Instagram @ilcalcio.amodomio: ~4000 follower, 277 post, reel narrativi/emotivi (600–900 visualizzazioni).
  La bio esiste già e cita **"Gli Imbattibili, il libro"** con link Amazon: non sostituirla.
  Il libro (Amazon) racconta la **stagione**; i PDF sono gli **allenamenti**: vanno presentati insieme
  ("il libro racconta cosa è successo, i PDF come ci siamo arrivati").
  TikTok @matteo.falleri: 18 follower, contenuti musicali (canzoni sue), non di calcio. Consigliato
  un account TikTok separato per il calcio: creato **@il.calcio.a.modo** ("Il Calcio a Modo Mio").
  Pubblicati: post 1 (cross) su Instagram e TikTok il 2/10/2026. Prossimi: gruppi Facebook, post 2 fra 3–4 giorni.
  Post 1 Instagram dopo poche ore: 558 visualizzazioni, 8 like, **9 salvataggi**, 4 visite al profilo
  (più dell'intero mese precedente, 507). I caroselli tecnici funzionano: continuare così.
  Alle 10:48: 843 visualizzazioni, 10 salvataggi, 1 condivisione, 9 visite al profilo, non follower 0,8%.
  Alle 11:43: 1220 visualizzazioni (483 account), 13 like, 11 salvataggi, 11 visite al profilo.
  Dopo ~28 ore (3/10 14:11): 2245 visualizzazioni (914 account), 23 like, **19 salvataggi**, 2 condivisioni,
  25 visite al profilo, **4 nuovi follower**, **2 tocchi sul link in bio**, non follower 15,1%, 0 commenti.
  Età: 35-44 36%, 45-54 31% → pubblico giusto (allenatori). Prossimi post: chiudere con domanda per i commenti.
  TikTok post 1: 0 visualizzazioni dopo 1h30 (account nuovo; impostazioni verificate, tutto pubblico).
  Ma il pubblico del carosello è 100% follower: per arrivare agli sconosciuti servono i **Reel**.
  Facebook: già membro di "ALLENATORI.. uno stile di vita" (2904 membri, privato) → primo gruppo dove pubblicare.
  allenatore.net (38k) e Club Allenatori Italiani (28k) sono **pagine**, non gruppi: lì non si pubblica
  (allenatore.net accetta contributi sul sito: idea per dopo). "Carriera allenatore Italia" = videogioco, scartato.
  Gruppi per gli esercizi (solo allenatori): Allenatori.. uno stile di vita (già dentro), ALLENATORI CALCIO
  (135k, privato), L'allenatore di Calcio (16.9k), Allenatori di base settore giovanile (18k, privato),
  A.A.C.I. Allenatori Associati Calcio Italiano (2.5k). Riserve: Allenatori di calcio (2k), Allenatori di calcio
  giovanile, Allenatori e preparatori atletici, Club Allenatori Italiani attività di base.
  Gruppi toscani (Calcio Dilettanti Toscana, Dilettanti e Giovanile Toscana) e "Il calcio in provincia": NON sono
  di allenatori (lo ha fatto notare lui) → solo per post sulla storia/libro. Non nel gruppo del Vaglia.
  3/10: accettato in ALLENATORI CALCIO, Allenatori di calcio, Allenatori di base settore giovanile.
  3/10 ore 14:07: post 1 (cross) pubblicato in ALLENATORI CALCIO. Alle 19: Allenatori.. uno stile di vita.
  Il secondo gruppo (Allenatori.. uno stile di vita) il 3/10 alle 19 NON è stato fatto: recuperarlo.
  4/10 ore 18:19: Reel cross anche su TikTok; il post foto TikTok è passato da 0 a 1 visualizzazione.
  4/10 ore 18:16: Reel cross pubblicato su Instagram (musica scelta da lui, prova e etichetta IA spente).
  Non pubblicare lo stesso post in tutti i gruppi insieme (filtro spam): 2–3 gruppi al giorno.
  Agenda (marketing/agenda-ottobre.ics, ore 21): sab 3 FB 2 gruppi · dom 4 Reel · lun 5 FB 2 gruppi ·
  mar 6 post 2 · mer 7 FB ultimo gruppo · ven 9 post 3.
- Prodotto in vendita: pacchetto "Gli Imbattibili · Il Precampionato" (primi 10 allenamenti in un unico PDF
  con copertina, indice e prefazione). L'allenatore vuole un prezzo basso: proposta 9,90 €.
  Allenamento 1 gratis come assaggio ("commenta PRECAMPIONATO" su Instagram).
- Idea dell'allenatore (2/10): pacchetto **"difesa di ferro"** con le sole esercitazioni difensive degli
  Allenamenti 1-10 in progressione (scivolamenti, spaccare la linea, sul lancio, lancio in esterna, Ti lascio alle
  spalle, 6c4, cross in diagonale invertita, 6c4 di verifica, uscite sul centrocampo, attacco-difesa, emergenza).
  Ripartire dalla bozza `prodotti/linea-difensiva/`. Prezzo proposto circa 5 € IVA inclusa.
  L'allenatore: per partire con la linea a 4 i primi 10 allenamenti coprono tutto; più avanti nella stagione
  lavora in inferiorità (4c6, 4c8, 4c11, 8c10). Proposta: Volume 1 "le basi della linea a 4" subito con gli 11
  esercizi; Volume 2 "difesa in inferiorità" quando arrivano quegli allenamenti (da chiedere dove sono).
- Divisione dei compiti (2/10): **Claude prepara** post, testi e PDF; **l'allenatore controlla e pubblica**.
  Per lui i post sono la priorità. Estero (inglese, poi magari spagnolo/portoghese) solo dopo che l'Italia funziona;
  adattare il gergo (suicidi, preventive, diagonale invertita), non tradurre parola per parola.
- Esperienza precedente: 5 mesi su Etsy senza vendite (solo annuncio, nessun traffico portato). Ora il traffico
  arriva da Instagram. **Controllo statistiche Etsy ogni settimana**; primo controllo insieme verso il 16/10/2026
  (screenshot di Statistiche: visite, provenienza, vendite). Il negozio aveva già 1 vendita con 5 stelle.
- **Collana "Gli Imbattibili"** (un'uscita alla volta, mai tutto insieme; ogni uscita = una notizia su Instagram):
  1. Il precampionato ✅ in vendita · 2. La linea a 4 (Vol. 1, proposta: uscita **fine ottobre**, dopo il lancio
  dell'Allenamento 1 gratis del 10-11/10 e il controllo Etsy del 16/10; preparare il PDF nella conversazione ALLENAMENTI) · 3. La difesa in
  inferiorità (Vol. 2, più avanti) · 4. Costruire un modello di gioco · altri temi da aggiungere quando li dice.
- **Seconda serie (futura)**: l'allenatore ha tutti gli allenamenti della passata stagione, campionato di
  **Terza Categoria vinto** con la prima squadra. Pubblico diverso (allenatori dilettanti). Da aprire solo dopo che
  la collana Gli Imbattibili cammina da sola; serviranno stagione, nome della serie e numeri del campionato.
- Più avanti: prefazione (mancano nome, società, stagione, numeri del campionato), pagina
  "Chi sono" con la figura intera (tagliare le scarpe: si vede il marchio Adidas), annunci Etsy,
  versione inglese.
