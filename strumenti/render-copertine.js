// Salva ogni copertina (.c5) di una pagina HTML come PNG ad alta risoluzione.
// Serve al pacchetto: le copertine con filtri e maschere pesano molto nel PDF,
// come immagini JPG restano nitide e leggere.
// Uso: NODE_PATH=$(npm root -g) node strumenti/render-copertine.js <file.html> <cartella>
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [html, cartella] = process.argv.slice(2);
  fs.mkdirSync(cartella, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2.5 });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const cop = await page.$$('section.c5');
  for (let i = 0; i < cop.length; i++) {
    await cop[i].screenshot({ path: path.join(cartella, `copertina-${String(i).padStart(2, '0')}.png`) });
  }
  console.log(`${cop.length} copertine in ${cartella}`);
  await browser.close();
})();
