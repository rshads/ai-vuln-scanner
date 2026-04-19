VULN_MAP = {
    "SQL Injection": {
        "explanation": "SQL Injection allows attackers to manipulate database queries by injecting malicious SQL. This can lead to data exfiltration, corruption, or bypassing authentication.",
        "suggestion": "Use parameterized database queries or ORM methods that safely escape user input. Never concatenate user input directly in database operations."
    },
    "Cross-Site Scripting (XSS)": {
        "explanation": "XSS lets attackers inject malicious scripts into web pages, which can steal user data or hijack sessions when viewed by others.",
        "suggestion": "Sanitize and escape all user-supplied input before rendering in the UI. Consider libraries that automatically handle output encoding."
    },
    "Command Injection": {
        "explanation": "Command Injection enables attackers to execute arbitrary system commands on your server, potentially resulting in complete system compromise.",
        "suggestion": "Never pass user input directly into system commands. Use high-level APIs or validate and sanitize inputs rigorously."
    },
    "Hardcoded Secret": {
        "explanation": "Hardcoded secrets in source code expose sensitive credentials and keys if the code is leaked or attacked.",
        "suggestion": "Store secrets in secure environment variables or use a secrets management tool. Avoid including passwords or API keys directly in code."
    },
    "Unsafe Function": {
        "explanation": "Use of known dangerous functions (e.g., eval, exec) can introduce severe security issues, as these can execute arbitrary code.",
        "suggestion": "Avoid using dangerous functions. Refactor code to use safe alternatives or restrict input to allowed operations only."
    },
    "Scan Error": {
        "explanation": "There was a problem running the vulnerability scan.",
        "suggestion": "Please try again. Ensure Semgrep is properly installed and the code is valid."
    }
}

def explain_vulns(results):
    explanations = []
    for res in results:
        base = VULN_MAP.get(res["type"], {
            "explanation": "No explanation available.",
            "suggestion": "Check documentation for remediation steps."
        })
        explanations.append({
            "type": res["type"],
            "file": res["file"],
            "line": res["line"],
            "severity": res["severity"],
            "explanation": base["explanation"],
            "suggestion": base["suggestion"]
        })
    return explanations
