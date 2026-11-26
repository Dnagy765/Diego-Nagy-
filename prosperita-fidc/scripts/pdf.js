// Gera o PDF e os prints de conferência a partir do HTML autocontido.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]); const shots = process.argv[3];
  const b = await chromium.launch(); const url = 'file://' + path.join(dir, 'Prosperita_FIDC_relatorio_final.html');
  const p = await b.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
  await p.route(/^https?:/, r => r.abort()); await p.goto(url);
  await p.pdf({ path: path.join(dir, 'Prosperita_FIDC_relatorio_final.pdf'), format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>', footerTemplate: '<div style="width:100%;font:9px Arial;color:#52606D;padding:0 14mm;display:flex;justify-content:space-between"><span>Prosperità FIDC · relatório final de diligência · 26/11/2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  if (shots) { await p.screenshot({ path: path.join(shots, 'desk.png') });
    const m = await b.newPage({ viewport: { width: 375, height: 800 }, deviceScaleFactor: 1 }); await m.goto(url); await m.screenshot({ path: path.join(shots, 'mob.png') });
    const sw = await m.evaluate(() => document.documentElement.scrollWidth); console.log('scrollWidth 375:', sw); }
  await b.close();
})();
