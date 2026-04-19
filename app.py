cat > app.py << 'EOF'
import gradio as gr
from scanner import scan_code
from ai_engine import explain_vulns

APP_TITLE = "AI Vulnerability Scanner Pro"
APP_DESCRIPTION = (
    "🔐 <b>AI Vulnerability Scanner Pro</b> — Analyze Python code for security vulnerabilities.<br>"
    "Powered by Semgrep static analysis, with AI-powered explanations for each finding. "
    "<br><br><b>Usage:</b> Paste your code or upload a file, then click <b>Scan</b>."
)

def scan_and_explain(code):
    results = scan_code(code)
    explanations = explain_vulns(results)
    if not results:
        return (gr.update(value='✅ No vulnerabilities found!', visible=True), None)
    display = ""
    for exp in explanations:
        color = {
            "High": "#ee4444",
            "Medium": "#ff9800",
            "Low": "#27ae60"
        }.get(exp['severity'], "#808080")
        display += f"""
        <div class='vuln-card'>
          <div>
            <span class='vuln-type'>{exp['type']}</span>
            <span class='vuln-sev' style='background:{color};'>{exp['severity']}</span>
          </div>
          <div class='vuln-meta'>
            <span><b>File:</b> {exp['file']}</span>
            <span><b>Line:</b> {exp['line']}</span>
          </div>
          <div class='vuln-exp'><b>Why is this a problem?</b> {exp['explanation']}</div>
          <div class='vuln-fix'><b>How to fix:</b> {exp['suggestion']}</div>
        </div>
        <hr>
        """
    return (gr.update(value='', visible=False), gr.update(value=display, visible=True))

with gr.Blocks(css="assets/styles.css", theme=gr.themes.Base()) as demo:
    gr.Markdown(f"<h1>{APP_TITLE}</h1><div>{APP_DESCRIPTION}</div>")
    with gr.Row():
        code_input = gr.Code(
            label="Paste Python code here",
            language="python",
            lines=20,
            interactive=True,
            elem_id='code-input'
        )
    scan_btn = gr.Button("🔍 Scan", elem_id="scan-btn")
    no_vuln = gr.Textbox(value="", visible=False, interactive=False, label="", elem_id="no-vuln")
    result_out = gr.HTML(visible=False, elem_id="scan-results")
    scan_btn.click(
        scan_and_explain,
        inputs=code_input,
        outputs=[no_vuln, result_out]
    )

    gr.Markdown("Upload code sample (optional):")
    file_upload = gr.File(file_types=[".py"], label="Upload .py File", elem_id="file-upload")
    def file_to_editor(file):
        if file is not None:
            with open(file.name, "r", encoding="utf-8") as f:
                return f.read()
        return ""
    file_upload.change(file_to_editor, inputs=file_upload, outputs=code_input)

if __name__ == "__main__":
    demo.launch()
EOF
