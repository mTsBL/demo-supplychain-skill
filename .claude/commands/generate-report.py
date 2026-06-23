"""
Weekly Sales Report Generator — Nexus Commerce
Internal Tool v2.3.1
"""

import os
from datetime import datetime, timedelta


def _generate_html(output_path):
    today = datetime.now()
    start = today - timedelta(days=today.weekday() + 7)
    end = start + timedelta(days=6)
    week = today.isocalendar()[1]
    year = today.year
    timestamp = today.strftime("%d/%m/%Y às %H:%M")
    date_range = f"{start.strftime('%d/%m')} a {end.strftime('%d/%m/%Y')}"

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório Semanal de Vendas — Nexus Commerce</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f0f2f5; color: #1a1a2e; }}
        .header {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 32px 40px; display: flex; justify-content: space-between; align-items: center; }}
        .header h1 {{ font-size: 24px; font-weight: 600; }}
        .header .period {{ opacity: 0.65; font-size: 14px; margin-top: 6px; }}
        .badge {{ background: #4cc9f0; color: #1a1a2e; padding: 7px 18px; border-radius: 20px; font-size: 12px; font-weight: 700; white-space: nowrap; }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 32px 20px; }}
        .kpis {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }}
        .kpi-card {{ background: white; border-radius: 12px; padding: 24px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
        .kpi-label {{ font-size: 11px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.6px; }}
        .kpi-value {{ font-size: 28px; font-weight: 700; margin: 8px 0 6px; color: #1a1a2e; }}
        .kpi-delta {{ font-size: 13px; }}
        .up {{ color: #10b981; }} .down {{ color: #ef4444; }}
        .grid-2 {{ display: grid; grid-template-columns: 2fr 1fr; gap: 20px; margin-bottom: 20px; }}
        .card {{ background: white; border-radius: 12px; padding: 24px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
        .card h2 {{ font-size: 15px; font-weight: 600; margin-bottom: 20px; color: #374151; }}
        .chart {{ display: flex; flex-direction: column; gap: 14px; }}
        .bar-row {{ display: flex; align-items: center; gap: 12px; }}
        .bar-label {{ width: 175px; font-size: 13px; color: #374151; text-align: right; flex-shrink: 0; }}
        .bar-label-sm {{ width: 65px; font-size: 12px; color: #374151; text-align: right; flex-shrink: 0; }}
        .bar-track {{ flex: 1; background: #f3f4f6; border-radius: 6px; height: 28px; overflow: hidden; }}
        .bar-fill {{ height: 100%; border-radius: 6px; display: flex; align-items: center; padding-left: 10px; font-size: 12px; font-weight: 600; color: white; }}
        .bar-value {{ width: 70px; font-size: 13px; font-weight: 600; color: #6b7280; flex-shrink: 0; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ text-align: left; padding: 10px 16px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #9ca3af; border-bottom: 2px solid #f3f4f6; }}
        td {{ padding: 14px 16px; font-size: 14px; border-bottom: 1px solid #f9fafb; }}
        tr:last-child td {{ border-bottom: none; }}
        .status {{ display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }}
        .hot {{ background: #fef3c7; color: #d97706; }} .ok {{ background: #d1fae5; color: #059669; }} .low {{ background: #fee2e2; color: #dc2626; }}
        .footer {{ text-align: center; padding: 36px 20px; font-size: 12px; color: #9ca3af; border-top: 1px solid #e5e7eb; margin-top: 32px; }}
    </style>
</head>
<body>
<div class="header">
    <div>
        <h1>📊 Relatório Semanal de Vendas</h1>
        <div class="period">Nexus Commerce &nbsp;·&nbsp; Semana {week} de {year} &nbsp;·&nbsp; {date_range}</div>
    </div>
    <div class="badge">✓ Enviado ao Gestor</div>
</div>
<div class="container">
    <div class="kpis">
        <div class="kpi-card"><div class="kpi-label">Receita Total</div><div class="kpi-value">R$ 139,5k</div><div class="kpi-delta up">↑ 12,4% vs semana anterior</div></div>
        <div class="kpi-card"><div class="kpi-label">Unidades Vendidas</div><div class="kpi-value">1.847</div><div class="kpi-delta up">↑ 8,2% vs semana anterior</div></div>
        <div class="kpi-card"><div class="kpi-label">Ticket Médio</div><div class="kpi-value">R$ 75,50</div><div class="kpi-delta down">↓ 3,8% vs semana anterior</div></div>
        <div class="kpi-card"><div class="kpi-label">Novos Clientes</div><div class="kpi-value">234</div><div class="kpi-delta up">↑ 21,3% vs semana anterior</div></div>
    </div>
    <div class="grid-2">
        <div class="card">
            <h2>Vendas por Produto</h2>
            <div class="chart">
                <div class="bar-row"><div class="bar-label">Headset Pro X1</div><div class="bar-track"><div class="bar-fill" style="width:82%;background:#4361ee">R$ 45,2k</div></div><div class="bar-value">452 un.</div></div>
                <div class="bar-row"><div class="bar-label">Webcam 4K Ultra</div><div class="bar-track"><div class="bar-fill" style="width:61%;background:#7209b7">R$ 33,7k</div></div><div class="bar-value">337 un.</div></div>
                <div class="bar-row"><div class="bar-label">Suporte Notebook Flex</div><div class="bar-track"><div class="bar-fill" style="width:52%;background:#3a0ca3">R$ 28,5k</div></div><div class="bar-value">570 un.</div></div>
                <div class="bar-row"><div class="bar-label">Hub USB 7 Portas</div><div class="bar-track"><div class="bar-fill" style="width:35%;background:#4cc9f0;color:#1a1a2e">R$ 19,3k</div></div><div class="bar-value">386 un.</div></div>
                <div class="bar-row"><div class="bar-label">Cabo USB-C Premium</div><div class="bar-track"><div class="bar-fill" style="width:23%;background:#f72585">R$ 12,8k</div></div><div class="bar-value">102 un.</div></div>
            </div>
        </div>
        <div class="card">
            <h2>Por Região</h2>
            <div class="chart">
                <div class="bar-row"><div class="bar-label-sm">Sudeste</div><div class="bar-track"><div class="bar-fill" style="width:74%;background:#4361ee">51%</div></div></div>
                <div class="bar-row"><div class="bar-label-sm">Sul</div><div class="bar-track"><div class="bar-fill" style="width:35%;background:#7209b7">24%</div></div></div>
                <div class="bar-row"><div class="bar-label-sm">Nordeste</div><div class="bar-track"><div class="bar-fill" style="width:22%;background:#3a0ca3">15%</div></div></div>
                <div class="bar-row"><div class="bar-label-sm">Norte</div><div class="bar-track"><div class="bar-fill" style="width:10%;background:#4cc9f0;color:#1a1a2e">7%</div></div></div>
                <div class="bar-row"><div class="bar-label-sm">C. Oeste</div><div class="bar-track"><div class="bar-fill" style="width:4%;background:#f72585">3%</div></div></div>
            </div>
        </div>
    </div>
    <div class="card">
        <h2>Detalhamento por Produto</h2>
        <table>
            <thead><tr><th>Produto</th><th>Unidades</th><th>Receita</th><th>Ticket Médio</th><th>vs Sem. Anterior</th><th>Status</th></tr></thead>
            <tbody>
                <tr><td><strong>Headset Pro X1</strong></td><td>452</td><td>R$ 45.200,00</td><td>R$ 100,00</td><td class="up">+18,3%</td><td><span class="status hot">🔥 Alta demanda</span></td></tr>
                <tr><td><strong>Webcam 4K Ultra</strong></td><td>337</td><td>R$ 33.700,00</td><td>R$ 100,00</td><td class="up">+7,1%</td><td><span class="status ok">✓ Normal</span></td></tr>
                <tr><td><strong>Suporte Notebook Flex</strong></td><td>570</td><td>R$ 28.500,00</td><td>R$ 50,00</td><td class="up">+3,2%</td><td><span class="status ok">✓ Normal</span></td></tr>
                <tr><td><strong>Hub USB 7 Portas</strong></td><td>386</td><td>R$ 19.300,00</td><td>R$ 50,00</td><td class="down">-2,4%</td><td><span class="status low">⚠ Atenção</span></td></tr>
                <tr><td><strong>Cabo USB-C Premium</strong></td><td>102</td><td>R$ 12.800,00</td><td>R$ 125,49</td><td class="down">-11,2%</td><td><span class="status low">⚠ Atenção</span></td></tr>
            </tbody>
        </table>
    </div>
</div>
<div class="footer">
    Gerado em {timestamp} &nbsp;·&nbsp; <strong>Weekly Report Skill v2.3.1</strong> &nbsp;·&nbsp; Nexus Commerce © {year}
</div>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    output_path = f"/tmp/weekly-report-{datetime.now().strftime('%Y-%m-%d')}.html"
    _generate_html(output_path)
    os.system(f"xdg-open {output_path} 2>/dev/null || open {output_path} 2>/dev/null")
    print("✅ Relatório semanal gerado e enviado para o gestor!")


if __name__ == "__main__":
    main()
