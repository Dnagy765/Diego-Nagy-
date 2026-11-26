"""Reextração independente do informe mensal FIDC a partir dos zips brutos.
Filtra por CNPJ (com e sem máscara) em QUALQUER coluna e, em separado, por nome, para pegar erros de filtro."""
import zipfile, glob, os, re, sys, csv, hashlib, io, json
RAW = sys.argv[1]; OUT = sys.argv[2]
CNPJS = {'fidc': ('53.033.766/0001-39','53033766000139'), 'fif': ('53.071.764/0001-34','53071764000134'),
         'consult': ('57.938.381/0001-71','57938381000171')}
res = {}   # tabela -> list of (competencia, zip, membro, header, row)
namehits = []
members_seen = {}
sha = {}
for z in sorted(glob.glob(os.path.join(RAW,'fidc','inf_mensal_fidc_*.zip'))):
    sha[os.path.basename(z)] = hashlib.sha256(open(z,'rb').read()).hexdigest()
    zf = zipfile.ZipFile(z)
    for m in zf.namelist():
        mm = re.match(r'inf_mensal_fidc_tab_(.+)_(\d{6})\.csv$', m)
        if not mm: print('membro inesperado', z, m); continue
        tab, comp = mm.group(1), mm.group(2)
        members_seen.setdefault(tab, set()).add(comp)
        if comp < '202312': continue
        data = zf.read(m).decode('latin-1')
        lines = data.split('\n')
        header = lines[0].rstrip('\r')
        for ln in lines[1:]:
            ln = ln.rstrip('\r')
            if not ln: continue
            hit_cnpj = any(c in ln for c in CNPJS['fidc'])
            if hit_cnpj:
                res.setdefault(tab, []).append((comp, os.path.basename(z), m, header, ln))
            elif 'PROSPERIT' in ln.upper():
                namehits.append((comp, m, ln[:200]))
            for k in ('fif','consult'):
                if any(c in ln for c in CNPJS[k]):
                    namehits.append((comp, m, k+' :: '+ln[:300]))
os.makedirs(OUT, exist_ok=True)
for tab, rows in res.items():
    headers = sorted(set(r[3] for r in rows), key=lambda h: min(r[0] for r in rows if r[3]==h))
    allcols = []
    for h in headers:
        for c in h.split(';'):
            if c not in allcols: allcols.append(c)
    with open(os.path.join(OUT, f'fidc_tab_{tab}.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['_comp','_zip','_membro']+allcols)
        for comp, zb, m, h, ln in sorted(rows):
            d = dict(zip(h.split(';'), ln.split(';')))
            if len(h.split(';')) != len(ln.split(';')): print('colunas != ', m, len(h.split(';')), len(ln.split(';')))
            w.writerow([comp, zb, m]+[d.get(c,'') for c in allcols])
    comps = sorted(set(r[0] for r in rows))
    print(f'tab {tab:6s} linhas={len(rows):4d} comps={len(comps)} {comps[0]}..{comps[-1]} headers_distintos={len(headers)}')
print('membros por tabela (competências >=202312 presentes nos zips):')
for tab, cs in sorted(members_seen.items()):
    cs2 = sorted(c for c in cs if c>='202312'); print(' ', tab, len(cs2), cs2[0], cs2[-1])
print('hits por nome sem CNPJ / outros CNPJs:', len(namehits))
for h in namehits[:40]: print('  ', h)
json.dump(sha, open(os.path.join(OUT,'sha_fidc.json'),'w'), indent=1)
