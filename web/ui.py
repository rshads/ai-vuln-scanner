import gradio as gr
from core.scanner import scan_code
from core.ai_engine import ai_explain
from core.report import generate_report

def run(code):
    findings = scan_code(code)
    return generate_report(findings, ai_explain)

ui = gr.Blocks(theme=gr.themes.Soft())

with ui:
    gr.Markdown("# 🛡 AI Security Scanner Enterprise")
    gr.Markdown("Professional Code Vulnerability Analysis System")

    code = gr.Textbox(lines=20, label="Source Code")
    btn = gr.Button("🚀 Run Security Scan")
    output = gr.Textbox(lines=25, label="Security Report")

    btn.click(run, inputs=code, outputs=output)

ui.launch()
