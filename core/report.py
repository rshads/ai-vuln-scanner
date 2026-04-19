def generate_report(findings, ai_engine):
    if not findings:
        return "✅ CLEAN CODE — No vulnerabilities detected."

    report = "🔐 ENTERPRISE SECURITY REPORT\n"
    report += "=" * 50 + "\n\n"

    for f in findings:
        ai = ai_engine(f)

        report += f"""
🚨 TYPE: {f['type']}
⚠ SEVERITY: {f['severity']}
📍 LINE: {f['line']}
💻 CODE: {f['code']}

🧠 DESCRIPTION:
{ai['description']}

🛠 FIX:
{ai['fix']}

--------------------------------------
"""

    return report
