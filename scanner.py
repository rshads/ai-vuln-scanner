import re

def scan_code(code):
    results = []
    lines = code.split("\n")

    for i, line in enumerate(lines, 1):

        # SQL Injection
        if re.search(r"SELECT .* (\"|')", line):
            results.append(("SQL Injection", "High", i, line))

        # Command Injection
        if "os.system" in line or "subprocess" in line:
            results.append(("Command Injection", "Critical", i, line))

        # XSS
        if "render_template_string" in line or "innerHTML" in line:
            results.append(("XSS", "High", i, line))

        # Eval danger
        if "eval(" in line or "exec(" in line:
            results.append(("Code Injection", "Critical", i, line))

        # Hardcoded secrets
        if re.search(r"password\s*=\s*['\"]", line):
            results.append(("Hardcoded Secret", "Medium", i, line))

    return results
