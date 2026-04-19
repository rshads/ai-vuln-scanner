import gradio as gr
from scanner import scan_files
from report import generate_report

def run(files):
    results = scan_files(files)
    return generate_report(results)

css = """
body { background-color: #0b1220; color: white; }
.gradio-container { max-width: 900px !important; margin: auto; }
h1 { color: #4cc9f0; text-align: center; }
"""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as app:

    gr.Markdown("# 🔐 AI Vulnerability Scanner PRO")
    gr.Markdown("Upload multiple Python files to scan for security vulnerabilities")

    file_input = gr.File(
        file_count="multiple",
        file_types=[".py"],
        label="📁 Upload Python Files"
    )

    scan_btn = gr.Button("🚀 Scan Files")

    output = gr.Textbox(
        label="📊 Security Report",
        lines=25
    )

    scan_btn.click(run, inputs=file_input, outputs=output)

app.launch()
