def scan_files(files):
    results = []

    for file in files:
        content = file.read().decode("utf-8", errors="ignore")
        lines = content.split("\n")

        for i, line in enumerate(lines, 1):

            line_lower = line.lower()

            # 🔴 Command Injection
            if "os.system" in line or "subprocess" in line:
                results.append({
                    "file": file.name,
                    "type": "Command Injection",
                    "severity": "CRITICAL",
                    "line": i,
                    "code": line.strip()
                })

            # 🔴 Code Injection
            if "eval(" in line or "exec(" in line:
                results.append({
                    "file": file.name,
                    "type": "Code Injection",
                    "severity": "CRITICAL",
                    "line": i,
                    "code": line.strip()
                })

            # 🔴 SQL Injection
            if "select" in line_lower and ("+" in line or "'" in line):
                results.append({
                    "file": file.name,
                    "type": "SQL Injection",
                    "severity": "HIGH",
                    "line": i,
                    "code": line.strip()
                })

            # 🟠 XSS
            if "render_template_string" in line:
                results.append({
                    "file": file.name,
                    "type": "XSS",
                    "severity": "HIGH",
                    "line": i,
                    "code": line.strip()
                })

            # 🟡 Hardcoded Secret
            if "password" in line_lower and "=" in line:
                results.append({
                    "file": file.name,
                    "type": "Hardcoded Secret",
                    "severity": "MEDIUM",
                    "line": i,
                    "code": line.strip()
                })

    return results
