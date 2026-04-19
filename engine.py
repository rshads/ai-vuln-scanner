def analyze_results(results):
    analyzed = []

    for r in results:
        vtype, severity, line, code = r

        fix_map = {
            "SQL Injection": "Use parameterized queries (prepared statements).",
            "Command Injection": "Never use os.system with user input.",
            "XSS": "Escape HTML output or use templating auto-escape.",
            "Code Injection": "Avoid eval/exec completely.",
            "Hardcoded Secret": "Use environment variables or secret manager."
        }

        desc_map = {
            "SQL Injection": "Attacker can manipulate database queries.",
            "Command Injection": "Attacker can execute system commands.",
            "XSS": "Attacker can inject scripts into web pages.",
            "Code Injection": "Arbitrary code execution risk.",
            "Hardcoded Secret": "Sensitive data exposed in code."
        }

        analyzed.append({
            "type": vtype,
            "severity": severity,
            "line": line,
            "code": code,
            "desc": desc_map.get(vtype, "Unknown issue"),
            "fix": fix_map.get(vtype, "Review code manually")
        })

    return analyzed
