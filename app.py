import gradio as gr
from scanner import scan_code
from engine import analyze_results
from report import generate_report

def run_scan(code):
    results = scan_code(code)
    analysis = analyze_results(results)
    report = generate_report(analysis)
    return report

ui = gr.Blocks(css="""
body {background:#0f172a;color:white;}
""")

with ui:
    gr.Markdown("# 🔐 AI Vulnerability Scanner PRO")
    gr.Markdown("Advanced Code Security Analysis Tool")

    code = gr.Textbox(lines=20, label="Paste Code Here")

    btn = gr.Button("🚀 Scan Code")

    output = gr.Textbox(label="Security Report", lines=25)

    btn.click(run_scan, inputs=code, outputs=output)

ui.launch()
