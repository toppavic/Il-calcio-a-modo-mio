// Converte una pagina HTML in PDF A4 e salva un'anteprima PNG di ogni pagina.
// Uso: NODE_PATH=$(npm root -g) node strumenti/render.js <file.html> [cartella-anteprime]
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const html = path.resolve(process.argv[2]);
  const anteprime = process.argv[3];
  const pdf = html.replace(/\.html$/, '.pdf');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: pdf, format: 'A4', printBackground: true, preferCSSPageSize: true });
  const pagine = await page.$$('.page');
  if (anteprime) {
    await page.setViewportSize({ width: 794, height: 1123 });
    for (let i = 0; i < pagine.length; i++) {
      await pagine[i].screenshot({ path: path.join(anteprime, `pagina-${i + 1}.png`) });
    }
  }
  console.log(`${pdf} · ${pagine.length} pagine`);
  await browser.close();
})();
