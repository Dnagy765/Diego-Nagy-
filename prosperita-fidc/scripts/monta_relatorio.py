"""Monta o relatório final: Markdown -> HTML autocontido (CSS e SVG embutidos, zero recurso externo) -> PDF (Chromium via Playwright)."""
import subprocess, sys, os, re
BASE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(BASE, '..', 'relatorio')
md = open(os.path.join(R, 'RELATORIO_FINAL.md'), encoding='utf-8').read()
def fig(m):
    svg = open(os.path.join(R, 'svg', m.group(1) + '.svg'), encoding='utf-8').read()
    return f'<figure>{svg}<figcaption>{m.group(2)}</figcaption></figure>'
tab = open(os.path.join(R, 'tab_A.md'), encoding='utf-8').read()
md = md.replace('[[TABELA_A]]', tab)
md = re.sub(r'^\[\[GRAFICO (\w+) \| (.+?)\]\]$', fig, md, flags=re.M)
body = subprocess.run(['pandoc', '-f', 'markdown+pipe_tables-smart', '-t', 'html5', '--wrap=none'], input=md, capture_output=True, text=True, check=True).stdout
body = re.sub(r'<colgroup>.*?</colgroup>', '', body, flags=re.S)  # largura automática das colunas
body = re.sub(r'<th(?! scope)', '<th scope="col"', body)
css = open(os.path.join(R, 'estilo.css'), encoding='utf-8').read()
html = f'<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><title>Prosperità FIDC: relatório final de diligência</title><style>{css}</style></head><body><main>{body}</main></body></html>'
out = os.path.join(R, 'Prosperita_FIDC_relatorio_final.html'); open(out, 'w', encoding='utf-8').write(html)
print('html', len(html), 'externos:', len(re.findall(r'(?:src|href)="https?://[^"]+\.(?:css|js|png|jpg|woff2?)', html)))
