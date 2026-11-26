"""Séries do PROSPERITÀ FIF MM CP (53.071.764/0001-34) a partir dos hits brutos de CDA e informe diário (out/cda/hits.csv)."""
import csv, sys, os, pandas as pd
HITS, OUT, PAINEL = sys.argv[1], sys.argv[2], sys.argv[3]
csv.field_size_limit(10**8)
rows = list(csv.DictReader(open(HITS, encoding='utf-8'), delimiter='\t'))
D = lambda r: dict(zip(r['header'].split(';'), r['linha'].split(';')))
pl = pd.DataFrame([D(r) for r in rows if 'cda_fi_PL' in r['membro']])
pl['comp'] = pl.DT_COMPTC.str[:4]+pl.DT_COMPTC.str[5:7]; pl = pl.set_index('comp')
m = pd.DataFrame(index=pl.index); m['fif_pl'] = pl.VL_PATRIM_LIQ.astype(float)
b2 = pd.DataFrame([D(r) for r in rows if 'BLC_2' in r['membro']]); b2['comp'] = b2.DT_COMPTC.str[:4]+b2.DT_COMPTC.str[5:7]
for c in ('QT_POS_FINAL','VL_MERC_POS_FINAL','VL_AQUIS_NEGOC'): b2[c] = pd.to_numeric(b2[c])
fd = b2[b2.CNPJ_FUNDO_CLASSE_COTA=='53.033.766/0001-39'].set_index('comp')
m['fif_qt_cotas_fidc'] = fd.QT_POS_FINAL; m['fif_vl_cotas_fidc'] = fd.VL_MERC_POS_FINAL; m['fif_aplic_no_fidc'] = fd.VL_AQUIS_NEGOC
m['fif_outras_cotas_caixa'] = b2[b2.CNPJ_FUNDO_CLASSE_COTA!='53.033.766/0001-39'].groupby('comp').VL_MERC_POS_FINAL.sum()
p = pd.read_csv(PAINEL, sep=';', index_col=0); p.index = p.index.astype(str)
m['fidc_pl'] = p.pl; m['fidc_qt_cotas'] = p.qt_cotas
m['pct_fidc_detido_pelo_fif'] = 100*m.fif_qt_cotas_fidc/m.fidc_qt_cotas
m['dif_valor_fif_menos_pl_fidc'] = m.fif_vl_cotas_fidc - m.fidc_pl
m['pct_pl_fif_em_fidc'] = 100*m.fif_vl_cotas_fidc/m.fif_pl
dd = pd.DataFrame([D(r) for r in rows if r['sub']=='diario'])
for c in ('VL_QUOTA','VL_PATRIM_LIQ','CAPTC_DIA','RESG_DIA'): dd[c] = pd.to_numeric(dd[c])
dd['comp'] = dd.DT_COMPTC.str[:4]+dd.DT_COMPTC.str[5:7]
g = dd.groupby('comp').agg(fif_cota_fim=('VL_QUOTA','last'), fif_captacao=('CAPTC_DIA','sum'), fif_resgate=('RESG_DIA','sum'), fif_cotistas_fim=('NR_COTST','last'), fif_dias_informe=('DT_COMPTC','count'))
m = m.join(g)
b8 = pd.DataFrame([D(r) for r in rows if 'BLC_8' in r['membro']]); b8['comp'] = b8.DT_COMPTC.str[:4]+b8.DT_COMPTC.str[5:7]; b8['v'] = pd.to_numeric(b8.VL_MERC_POS_FINAL)
b8.groupby(['comp','TP_APLIC','DS_ATIVO']).v.sum().reset_index().to_csv(os.path.join(OUT,'fif_cda_demais_itens.csv'), sep=';', index=False)
m.round(6).to_csv(os.path.join(OUT,'fif_mensal.csv'), sep=';')
pd.set_option('display.width',250); pd.set_option('display.float_format', lambda v: f'{v:,.2f}')
print(m[['fif_pl','fif_vl_cotas_fidc','pct_fidc_detido_pelo_fif','dif_valor_fif_menos_pl_fidc','pct_pl_fif_em_fidc','fif_cota_fim','fif_cotistas_fim']].iloc[[0,6,12,13,20,22,23,24,25]].to_string())
print('captação FIF (14 meses coletados):', g.fif_captacao.sum(), '| aplicado no FIDC no mesmo período:', m.fif_aplic_no_fidc.loc[:'202501'].sum())
fees = b8[b8.TP_APLIC=='Valores a pagar'].groupby('comp').v.sum(); print('FIF valores a pagar (provisões de taxas) médio mensal:', round(fees.mean(),2), 'máx', fees.max())
