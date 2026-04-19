import gradio as gr
from scanner import scan_code
from ai_engine import explain

def analyze(code):
    results = scan_code(code)
    return explain(results)

ui = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=20, label="Paste Python Code"),
    outputs=gr.Textbox(label="Security Report"),
    title="🔐 AI Vulnerability Scanner (Windows Edition)",
    description="Detect security issues in Python code"
)

ui.launch()
