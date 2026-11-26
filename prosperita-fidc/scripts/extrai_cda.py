"""Varre CDA e informe diário brutos: linhas do FIF (53.071.764/0001-34) e qualquer linha de QUALQUER fundo
que cite o FIDC (53.033.766/0001-39), o FIF ou a consultoria — identifica cotistas-fundo."""
import zipfile, glob, os, sys, csv, io, hashlib, json
RAW, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
KEYS = {b'53.033.766/0001-39':'FIDC', b'53033766000139':'FIDC', b'53.071.764/0001-34':'FIF', b'53071764000134':'FIF',
        b'57.938.381/0001-71':'CONSULT', b'57938381000171':'CONSULT'}
rows = []; sha = {}; members = {}
for sub, pat in (('cda','cda_fi_*.zip'), ('diario','inf_diario_fi_*.zip')):
    for z in sorted(glob.glob(os.path.join(RAW, sub, pat))):
        zb = os.path.basename(z)
        h = hashlib.sha256()
        with open(z,'rb') as f:
            for chunk in iter(lambda: f.read(1<<20), b''): h.update(chunk)
        sha[zb] = h.hexdigest()
        zf = zipfile.ZipFile(z)
        members[zb] = zf.namelist()
        for m in zf.namelist():
            with zf.open(m) as f:
                header = f.readline().rstrip(b'\r\n').decode('latin-1')
                n = 0
                for ln in f:
                    n += 1
                    for k, tag in KEYS.items():
                        if k in ln:
                            rows.append((sub, zb, m, tag, header, ln.rstrip(b'\r\n').decode('latin-1')))
                            break
        print(zb, 'ok', flush=True)
with open(os.path.join(OUT,'hits.csv'),'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['sub','zip','membro','tag','header','linha'])
    w.writerows(rows)
json.dump({'sha':sha,'members':members}, open(os.path.join(OUT,'meta.json'),'w'), indent=1)
print('hits', len(rows))
