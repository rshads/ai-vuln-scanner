def generate_report(results):

    if not results:
        return "✅ No vulnerabilities found. Code looks clean."

    report = "🔐 SECURITY SCAN REPORT\n"
    report += "=" * 60 + "\n\n"

    for r in results:

        color = {
            "CRITICAL": "🔴",
            "HIGH": "🟠",
            "MEDIUM": "🟡"
        }.get(r["severity"], "⚪")

        report += f"""
📁 File: {r['file']}
{color} Type: {r['type']}
⚠ Severity: {r['severity']}
📍 Line: {r['line']}
💻 Code: {r['code']}

💡 Recommendation:
Fix this issue to improve security.

----------------------------------------
"""

    # Summary
    total = len(results)
    critical = len([r for r in results if r["severity"] == "CRITICAL"])
    high = len([r for r in results if r["severity"] == "HIGH"])

    report += f"""

📊 SUMMARY
Total Issues: {total}
Critical: {critical}
High: {high}
"""

    return report
