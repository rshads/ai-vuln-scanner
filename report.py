def generate_report(data):
    if not data:
        return "✅ No vulnerabilities detected. Code is clean."

    report = "🔐 SECURITY ANALYSIS REPORT\n"
    report += "="*40 + "\n\n"

    for item in data:
        report += f"""
🔴 Type: {item['type']}
⚠ Severity: {item['severity']}
📍 Line: {item['line']}
💻 Code: {item['code']}

🧠 Description:
{item['desc']}

🛠 Fix:
{item['fix']}

------------------------------------
"""

    return report
