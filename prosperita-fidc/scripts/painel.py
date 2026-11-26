"""Painel mensal do PROSPERITÀ FIDC a partir da reextração própria dos zips da CVM (out/fidc) e do CDI bruto do BCB."""
import pandas as pd, json, sys, os
SRC, RAW, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
R = lambda t: pd.read_csv(f'{SRC}/fidc_tab_{t}.csv', sep=';', dtype=str).fillna('')
f = lambda s: pd.to_numeric(s, errors='coerce')
I = R('I').set_index('_comp'); III = R('III').set_index('_comp'); IV = R('IV').set_index('_comp')
V = R('V').set_index('_comp'); VII = R('VII').set_index('_comp'); IX = R('IX').set_index('_comp')
p = pd.DataFrame(index=I.index)
p['admin'] = I.ADMIN.str.split().str[0]
p['pl'] = f(IV.TAB_IV_A_VL_PL); p['ativo'] = f(I.TAB_I_VL_ATIVO); p['passivo'] = f(III.TAB_III_VL_PASSIVO)
p['dc_a_vencer'] = f(I.TAB_I2A1_VL_CRED_VENC_AD); p['dc_inad'] = f(I.TAB_I2A3_VL_CRED_INAD); p['pdd'] = f(I.TAB_I2A11_VL_REDUCAO_RECUP)
p['dc_bruto'] = p.dc_a_vencer + p.dc_inad; p['dc_liq'] = f(I.TAB_I2A_VL_DIRCRED_RISCO)
p['disp'] = f(I.TAB_I1_VL_DISP); p['cotas_fif'] = f(I.TAB_I2C5_VL_COTA_FIF); p['tpf'] = f(I.TAB_I2D_VL_TITPUB_FED); p['outros'] = f(I.TAB_I4_VL_OUTRO_ATIVO)
p['caixa'] = p.disp + p.cotas_fif + p.tpf
p['pct_dc_liq_pl'] = 100*p.dc_liq/p.pl; p['pct_caixa_pl'] = 100*p.caixa/p.pl
p['cedente1_cnpj'] = I.TAB_I2A12_CPF_CNPJ_CEDENTE_1; p['cedente1_pct'] = f(I.TAB_I2A12_PR_CEDENTE_1)
# cotas (classe única reportada ora como subordinada ora como sênior)
def cls(s): return 'SR' if ('Senior' in s or 'Sênior' in s) else 'SUB'
def piv(t, col):
    d = R(t); d['c'] = d.TAB_X_CLASSE_SERIE.map(cls); d[col] = f(d[col])
    return d.pivot(index='_comp', columns='c', values=col)
q = piv('X_2','TAB_X_QT_COTA'); vc = piv('X_2','TAB_X_VL_COTA'); rt = piv('X_3','TAB_X_VL_RENTAB_MES'); nc = piv('X_1','TAB_X_NR_COTST')
pick = lambda d: d['SUB'].where(d['SUB'].fillna(0) != 0, d['SR'])
p['qt_cotas'] = pick(q); p['vl_cota'] = pick(vc); p['rent_mes_informada'] = pick(rt); p['cotistas'] = nc.fillna(0).sum(axis=1)
p['classe_informada'] = ['SUB' if (q.loc[i,'SUB'] if pd.notna(q.loc[i,'SUB']) else 0) != 0 else 'SR' for i in p.index]
p['rent_mes_calc'] = 100*(p.vl_cota/p.vl_cota.shift(1) - 1); p.loc[p.index[0],'rent_mes_calc'] = 100*(p.vl_cota.iloc[0]/1000 - 1)
p['pl_check'] = p.qt_cotas*p.vl_cota - p.pl
x4 = R('X_4'); x4['v'] = f(x4.TAB_X_VL_TOTAL)
g = x4.groupby(['_comp','TAB_X_TP_OPER']).v.sum().unstack().fillna(0)
p['captacao'] = g['Captações no Mês']; p['amortizacao'] = g['Amortizações']; p['resgate'] = g['Resgates no Mês']
p['aquis_qtd'] = f(VII.TAB_VII_A1_1_QT_DIRCRED_RISCO); p['aquis_valor'] = f(VII.TAB_VII_A1_2_VL_DIRCRED_RISCO)
oth = [c for c in VII.columns if c.startswith('TAB_VII') and not c.startswith('TAB_VII_A')]
p['alien_recompra_subst'] = sum(f(VII[c]) for c in oth)
for k,c in (('tx_min','MIN'),('tx_med','MEDIA'),('tx_max','MAX')):
    col = [x for x in IX.columns if x.startswith('TAB_IX_A1_1') and x.endswith('COMPRA_'+c)][0]; p[k] = f(IX[col])
# aging
for n in ('30','60','90','120','150','180','360'): p['inad_'+n] = f(V[f'TAB_V_B{["30","60","90","120","150","180","360"].index(n)+1}_VL_INAD_{n}'])
p['inad_gt90'] = p[['inad_120','inad_150','inad_180','inad_360']].sum(axis=1)
vcols = {'30':'A1','60':'A2','90':'A3','120':'A4','150':'A5','180':'A6','360':'A7','720':'A8','1080':'A9'}
for n,a in vcols.items(): p['avenc_'+n] = f(V[f'TAB_V_{a}_VL_PRAZO_VENC_{n}'])
p['avenc_gt1080'] = f(V.TAB_V_A10_VL_PRAZO_VENC_MAIOR_1080)
p['prepago'] = f(V.TAB_V_C_VL_DIRCRED_ANTECIPADO)
p['pct_inad_bruto'] = 100*p.dc_inad/p.dc_bruto; p['pct_pdd_bruto'] = 100*p.pdd/p.dc_bruto; p['pdd_sobre_inad'] = p.pdd/p.dc_inad
# resultado
p['resultado'] = p.pl.diff() - p.captacao + p.amortizacao + p.resgate; p.loc[p.index[0],'resultado'] = p.pl.iloc[0] - p.captacao.iloc[0]
p['delta_pdd'] = p.pdd.diff().fillna(p.pdd.iloc[0]); p['resultado_ex_pdd'] = p.resultado + p.delta_pdd
p['resultado_ex_pdd_pct_pl_ini'] = 100*p.resultado_ex_pdd/p.pl.shift(1)
# CDI
raw = json.load(open(os.path.join(RAW,'bcb/sgs_12.json'))); m = {}
for r in raw:
    d,mo,y = r['data'].split('/'); k = y+mo; m[k] = m.get(k,1.0)*(1+float(r['valor'])/100)
# fundo começou em 28/12/2023: CDI de dezembro só a partir de 28/12
dez = 1.0
for r in raw:
    d,mo,y = r['data'].split('/')
    if y=='2023' and mo=='12' and int(d) >= 28: dez *= 1+float(r['valor'])/100
m['202312'] = dez
p['cdi_mes'] = [100*(m[i]-1) for i in p.index]
p['cota_acum'] = 100*(p.vl_cota/1000 - 1); p['cdi_acum'] = 100*((1+p.cdi_mes/100).cumprod() - 1)
p['fundo_acum_encadeado'] = 100*((1+p.rent_mes_informada/100).cumprod() - 1)  # usa a rentabilidade informada, que neutraliza a amortização de 10/2025
p.round(6).to_csv(os.path.join(OUT,'painel_mensal_fidc.csv'), sep=';')
print('painel gravado:', len(p), 'meses', p.index[0], p.index[-1])
