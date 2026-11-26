"""Gráficos em SVG (sem dependências) para o relatório final. Lê o painel mensal e o diário do FIF."""
import csv, sys, os, json
PAINEL, DIARIO, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
G, T2, BORDA, AZUL, CRIT, ATEN, SUC = '#333333', '#52606D', '#D9DED4', '#1D4ED8', '#B42318', '#8A5A00', '#166534'
def br(v, d=0):
    return f'{v:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
P = list(csv.DictReader(open(PAINEL, encoding='utf-8'), delimiter=';'))
key = list(P[0].keys())[0]
comp = [r[key] for r in P]; f = lambda k: [float(r[k]) if r[k] not in ('', 'nan') else 0.0 for r in P]
lab = lambda c: f'{c[4:]}/{c[2:4]}'
W, H, ML, MR, MT, MB = 720, 300, 52, 96, 16, 34
def frame(ymin, ymax, ticks, fmt, xs_labels, body, title, desc, w=W, h=H, mr=MR):
    pw, ph = w - ML - mr, h - MT - MB
    y = lambda v: MT + ph * (1 - (v - ymin) / (ymax - ymin))
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title><desc>{desc}</desc>']
    for t in ticks:
        s.append(f'<line x1="{ML}" x2="{w-mr}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{BORDA}" stroke-width="{1.2 if t==0 else 0.7}"/>')
        s.append(f'<text x="{ML-6}" y="{y(t)+4:.1f}" text-anchor="end" font-size="12" fill="{T2}">{fmt(t)}</text>')
    for xpos, text in xs_labels:
        s.append(f'<text x="{xpos:.1f}" y="{h-10}" text-anchor="middle" font-size="12" fill="{T2}">{text}</text>')
    s.append(body(y, pw, ph)); s.append('</svg>')
    return '\n'.join(s)
def xlin(n, pw): return lambda i: ML + pw * i / (n - 1)
def path(xs, ys): return 'M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in zip(xs, ys))
def xlabels(n, pw, every, labs, off=0): return [(ML + pw * i / (n - 1), labs[i]) for i in range(off, n, every)]
out = {}
# 1. cota x CDI
fa, ca = f('fundo_acum_encadeado'), f('cdi_acum'); n = len(comp); pw = W - ML - MR
def b1(y, pw, ph):
    x = xlin(n, pw); xs = [x(i) for i in range(n)]
    s = f'<path d="{path(xs,[y(v) for v in ca])}" fill="none" stroke="{T2}" stroke-width="2"/>'
    s += f'<path d="{path(xs,[y(v) for v in fa])}" fill="none" stroke="{AZUL}" stroke-width="2.5"/>'
    s += f'<text x="{xs[-1]+6}" y="{y(ca[-1])+4:.1f}" font-size="12" font-weight="600" fill="{T2}">CDI {br(ca[-1],1)}%</text>'
    s += f'<text x="{xs[-1]+6}" y="{y(fa[-1])+4:.1f}" font-size="12" font-weight="600" fill="{AZUL}">Fundo {br(fa[-1],1)}%</text>'
    i = comp.index('202603'); s += f'<circle cx="{xs[i]:.1f}" cy="{y(fa[i]):.1f}" r="3.5" fill="{AZUL}"/><text x="{xs[i]-8:.1f}" y="{y(fa[i])+16:.1f}" text-anchor="end" font-size="12" fill="{G}">03/2026: {br(fa[i],1)}%</text>'
    return s
out['g1'] = frame(-40, 50, [-40, -20, 0, 20, 40], lambda t: f'{t}%', xlabels(n, pw, 6, [lab(c) for c in comp]), b1, 'Rentabilidade acumulada do fundo e do CDI', 'Linha do fundo e linha do CDI, de dezembro de 2023 a outubro de 2026.')
# 2. PL: DC líquido e caixa
dc, cx, pl = [v/1e6 for v in f('dc_liq')], [v/1e6 for v in f('caixa')], [v/1e6 for v in f('pl')]
def b2(y, pw, ph):
    bw = pw / n * 0.72; s = ''
    for i in range(n):
        x0 = ML + pw * (i + 0.14) / n
        s += f'<rect x="{x0:.1f}" y="{y(dc[i]):.1f}" width="{bw:.1f}" height="{y(0)-y(dc[i]):.1f}" fill="{G}"/>'
        s += f'<rect x="{x0:.1f}" y="{y(dc[i]+cx[i]):.1f}" width="{bw:.1f}" height="{max(0,y(dc[i])-y(dc[i]+cx[i])-1):.1f}" fill="{AZUL}"/>'
    xe = W - MR + 6
    s += f'<text x="{xe}" y="{y(dc[-1]+cx[-1]/2)+4:.1f}" font-size="12" font-weight="600" fill="{AZUL}">Caixa</text><text x="{xe}" y="{y(dc[-1]/2)+4:.1f}" font-size="12" font-weight="600" fill="{G}">Créditos</text>'
    for c, txt in (('202508', 'último aporte'),):
        i = comp.index(c); xx = ML + pw * (i + 0.5) / n
        s += f'<line x1="{xx:.1f}" x2="{xx:.1f}" y1="{MT+12}" y2="{y(dc[i]+cx[i])-3:.1f}" stroke="{T2}" stroke-dasharray="3 3"/><text x="{xx:.1f}" y="{MT+8}" text-anchor="middle" font-size="12" fill="{G}">{txt}, 08/25</text>'
    return s
out['g2'] = frame(0, 10, [0, 2, 4, 6, 8, 10], lambda t: f'{t}', [(ML + pw * (i + 0.5) / n, lab(comp[i])) for i in range(0, n, 6)], b2, 'Ativo do fundo em R$ milhões: créditos líquidos de provisão e caixa', 'Barras empilhadas mensais de créditos e caixa.')
# 3. vencidos e PDD % carteira
i0 = comp.index('202410'); cc = comp[i0:]; vi, pd = f('pct_inad_bruto')[i0:], f('pct_pdd_bruto')[i0:]; m = len(cc)
def b3(y, pw, ph):
    x = xlin(m, pw); xs = [x(i) for i in range(m)]
    s = f'<path d="{path(xs,[y(v) for v in vi])}" fill="none" stroke="{ATEN}" stroke-width="2.5"/><path d="{path(xs,[y(v) for v in pd])}" fill="none" stroke="{CRIT}" stroke-width="2.5"/>'
    s += f'<text x="{xs[-1]+6}" y="{y(vi[-1])-2:.1f}" font-size="12" font-weight="600" fill="{ATEN}">Vencidos {br(vi[-1],1)}%</text><text x="{xs[-1]+6}" y="{y(pd[-1])+12:.1f}" font-size="12" font-weight="600" fill="{CRIT}">Provisão {br(pd[-1],1)}%</text>'
    j = cc.index('202603'); s += f'<text x="{xs[j]:.1f}" y="{y(pd[j])-6:.1f}" text-anchor="middle" font-size="12" fill="{G}">03/2026: provisão de {br(pd[j],1)}%</text>'
    j = cc.index('202508'); s += f'<text x="{xs[j]:.1f}" y="{y(vi[j])-6:.1f}" text-anchor="middle" font-size="12" fill="{G}">08/2025: {br(vi[j],1)}%</text>'
    return s
out['g3'] = frame(0, 40, [0, 10, 20, 30, 40], lambda t: f'{t}%', xlabels(m, pw, 4, [lab(c) for c in cc]), b3, 'Vencidos e provisão em % da carteira bruta', 'Duas linhas mensais de outubro de 2024 a outubro de 2026.')
# 4. cota diária do FIF
D = [r for r in csv.DictReader(open(DIARIO, encoding='utf-8'), delimiter=';') if '2025-06-01' <= r['DT_COMPTC'] <= '2026-01-30']
q = [float(r['VL_QUOTA']) for r in D]; dts = [r['DT_COMPTC'] for r in D]; k = len(q)
def b4(y, pw, ph):
    x = xlin(k, pw); xs = [x(i) for i in range(k)]
    s = f'<path d="{path(xs,[y(v) for v in q])}" fill="none" stroke="{AZUL}" stroke-width="2"/>'
    for d, txt, dy in (('2025-12-22', 'mínima em 22/12: 782', 16), ('2026-01-29', '29/01: 804', 16), ('2026-01-30', '30/01: 911', -8)):
        i = dts.index(d); anc = 'end' if d >= '2026-01-29' else 'middle'
        s += f'<circle cx="{xs[i]:.1f}" cy="{y(q[i]):.1f}" r="3" fill="{AZUL}"/><text x="{xs[i]-(6 if anc=="end" else 0):.1f}" y="{y(q[i])+dy:.1f}" text-anchor="{anc}" font-size="12" fill="{G}">{txt}</text>'
    return s
mlab = []; seen = set()
for i, d in enumerate(dts):
    if d[:7] not in seen: seen.add(d[:7]); mlab.append((ML + pw * i / (k - 1), f'{d[5:7]}/{d[2:4]}'))
out['g4'] = frame(760, 940, [760, 800, 840, 880, 920], lambda t: f'{t}', mlab[1:], b4, 'Cota diária do FIF, que detinha 100% das cotas do FIDC', 'Linha diária de junho de 2025 a janeiro de 2026.', mr=24)
# 5. custo fixo % PL por tamanho
def custo(plm, piso=336.0, pct=0.005, outros=40.0): return 100 * (max(piso, pct * plm * 1000) + outros) / (plm * 1000)
xsv = [5 + i * 0.5 for i in range(0, 151)]
def b5(y, pw, ph):
    x = lambda v: ML + pw * (v - 5) / 75
    s = f'<path d="{path([x(v) for v in xsv],[y(custo(v)) for v in xsv])}" fill="none" stroke="{G}" stroke-width="2.5"/>'
    for v, anc in ((8.8, 'start'), (20, 'start'), (30, 'start'), (50, 'start'), (80, 'end')):
        s += f'<circle cx="{x(v):.1f}" cy="{y(custo(v)):.1f}" r="3.5" fill="{CRIT if v<10 else G}"/><text x="{x(v)+(8 if anc=="start" else -8):.1f}" y="{y(custo(v))-8:.1f}" text-anchor="{anc}" font-size="12" font-weight="600" fill="{CRIT if v<10 else G}">R$ {br(v,1 if v<10 else 0)} mi: {br(custo(v),1)}%</text>'
    return s
out['g5'] = frame(0, 8, [0, 2, 4, 6, 8], lambda t: f'{t}%', [(ML + (W - ML - 24) * (v - 5) / 75, f'{v}') for v in (10, 20, 30, 40, 50, 60, 70, 80)], b5, 'Custo fixo anual em % do PL conforme o tamanho do fundo', 'Curva decrescente do custo fixo em relação ao patrimônio.', mr=24)
for kx, v in out.items(): open(os.path.join(OUT, kx + '.svg'), 'w', encoding='utf-8').write(v)
print({k: len(v) for k, v in out.items()}, 'custo 8.8/20/30/50:', [round(custo(v), 2) for v in (8.8, 20, 30, 50)])
