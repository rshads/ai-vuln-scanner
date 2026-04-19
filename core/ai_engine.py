def ai_explain(vuln):
    explanations = {
        "SQL Injection": "Database query can be manipulated by attacker input.",
        "Command Injection": "System commands executed from unsafe input.",
        "XSS": "Script injection into web pages.",
        "Code Injection": "Execution of arbitrary code.",
        "Hardcoded Secret": "Sensitive credentials exposed in source code."
    }

    fixes = {
        "SQL Injection": "Use parameterized queries / ORM.",
        "Command Injection": "Never pass user input to shell commands.",
        "XSS": "Escape output or use auto-escaping frameworks.",
        "Code Injection": "Remove eval/exec usage completely.",
        "Hardcoded Secret": "Use environment variables or secret vaults."
    }

    return {
        "description": explanations.get(vuln["type"], "Unknown issue"),
        "fix": fixes.get(vuln["type"], "Manual review required")
    }
