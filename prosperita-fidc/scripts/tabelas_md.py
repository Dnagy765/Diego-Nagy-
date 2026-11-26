"""Gera as tabelas markdown do relatório a partir do painel mensal."""
import pandas as pd, sys
p = pd.read_csv(sys.argv[1], sep=';', index_col=0); p.index = p.index.astype(str); OUT = sys.argv[2]
def n(v, d=0):
    if pd.isna(v): return '–'
    s = f'{v:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return s
c = lambda i: f'{i[4:]}/{i[:4]}'
k = lambda v: n(v/1000, 0)
A = ['| Mês | PL (R$ mil) | Cota (R$) | Rent. mês | CDI mês | Fundo acum. | CDI acum. | Cotistas | Adm. |', '|---|---:|---:|---:|---:|---:|---:|---:|---|']
for i, r in p.iterrows():
    A.append(f'| {c(i)} | {k(r.pl)} | {n(r.vl_cota,2)} | {n(r.rent_mes_informada,2)}% | {n(r.cdi_mes,2)}% | {n(r.fundo_acum_encadeado,2)}% | {n(r.cdi_acum,2)}% | {int(r.cotistas)} | {r.admin} |')
B = ['| Mês | PL | DC líquido | DC/PL | Caixa | Caixa/PL | Aquisições (qtd) | Aquisições (R$ mil) | Captação | Amortização | Valores a pagar |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for i, r in p.iterrows():
    B.append(f'| {c(i)} | {k(r.pl)} | {k(r.dc_liq)} | {n(r.pct_dc_liq_pl,1)}% | {k(r.caixa)} | {n(r.pct_caixa_pl,1)}% | {int(r.aquis_qtd)} | {k(r.aquis_valor)} | {k(r.captacao) if r.captacao else "–"} | {k(r.amortizacao) if r.amortizacao else "–"} | {k(r.passivo)} |')
C = ['| Mês | Carteira bruta | Vencidos | % | 1–30d | 31–60d | 61–90d | >90d | PDD | PDD/carteira | PDD/vencidos | Taxa mín/méd/máx | Resultado | Var. PDD | Resultado ex-PDD |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|']
for i, r in p.loc['202410':].iterrows():
    tx = f'{n(r.tx_min,1)} / {n(r.tx_med,1)} / {n(r.tx_max,1)}' if r.tx_med else '–'
    C.append(f'| {c(i)} | {k(r.dc_bruto)} | {k(r.dc_inad)} | {n(r.pct_inad_bruto,1)}% | {k(r.inad_30)} | {k(r.inad_60)} | {k(r.inad_90)} | {k(r.inad_gt90)} | {k(r.pdd)} | {n(r.pct_pdd_bruto,1)}% | {n(100*r.pdd_sobre_inad,0)}% | {tx} | {k(r.resultado)} | {k(r.delta_pdd)} | {k(r.resultado_ex_pdd)} |')
for nm, t in (('A', A), ('B', B), ('C', C)): open(f'{OUT}/tab_{nm}.md', 'w').write('\n'.join(t) + '\n')
print(A[2]); print(A[-1]); print(B[-1]); print(C[-1])
