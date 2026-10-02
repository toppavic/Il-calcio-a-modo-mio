// Salva ogni .slide (2000×1500) di una pagina HTML come PNG per le foto dell'annuncio Etsy.
// Uso: NODE_PATH=$(npm root -g) node strumenti/render-etsy.js <file.html> <cartella>
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [html, cartella] = process.argv.slice(2);
  fs.mkdirSync(cartella, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2000, height: 1500 } });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const slide = await page.$$('.slide');
  for (let i = 0; i < slide.length; i++) {
    await slide[i].screenshot({ path: path.join(cartella, `etsy-${i + 1}.png`) });
  }
  console.log(`${slide.length} immagini in ${cartella}`);
  await browser.close();
})();
