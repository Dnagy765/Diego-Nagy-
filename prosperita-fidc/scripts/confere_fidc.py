import csv, sys, os, glob, json, hashlib
MINE, SOUL = sys.argv[1], sys.argv[2]
def load(p, enc):
    with open(p, encoding=enc, newline='') as f:
        r = list(csv.reader(f, delimiter=';'))
    return r[0], r[1:]
tot_div = 0
for p in sorted(glob.glob(os.path.join(MINE,'fidc_tab_*.csv'))):
    tab = os.path.basename(p)[len('fidc_tab_'):-4]
    sp = os.path.join(SOUL, f'inf_mensal_fidc_tab_{tab.lower()}.csv')
    if not os.path.exists(sp): print('AUSENTE no Soul:', tab); continue
    hm, rm = load(p, 'utf-8'); hs, rs = load(sp, 'utf-8-sig')
    cm = [c for c in hm if not c.startswith('_')]; cs = [c for c in hs if not c.startswith('_')]
    only_m = [c for c in cm if c not in cs]; only_s = [c for c in cs if c not in cm]
    im = {c:i for i,c in enumerate(hm)}; is_ = {c:i for i,c in enumerate(hs)}
    common = [c for c in cm if c in cs]
    key = lambda row, idx: tuple(row[idx[c]] for c in common)
    A = sorted(key(r, im) for r in rm); B = sorted(key(r, is_) for r in rs)
    ndiv = sum(1 for a,b in zip(A,B) if a!=b) + abs(len(A)-len(B))
    tot_div += ndiv
    print(f'{tab:6s} meu={len(rm):4d} soul={len(rs):4d} cols={len(common):3d} so_meu={only_m} so_soul={only_s} linhas_divergentes={ndiv}')
print('TOTAL divergências:', tot_div)
# sha256 dos zips x fontes_bloco1
sha = json.load(open(os.path.join(MINE,'sha_fidc.json')))
src = {}
with open(os.path.join(SOUL,'fontes_bloco1.csv'), encoding='utf-8-sig') as f:
    for r in csv.DictReader(f, delimiter=';'): src[os.path.basename(r['arquivo'])] = r
bad = [k for k,v in sha.items() if src.get(k,{}).get('sha256') != v]
print('sha256 zips conferidos:', len(sha), 'divergentes:', bad)
