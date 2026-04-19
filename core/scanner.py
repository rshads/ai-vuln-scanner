import re
from .severity import calculate_severity

def scan_code(code):
    findings = []
    lines = code.split("\n")

    for i, line in enumerate(lines, 1):

        checks = [
            ("SQL Injection", r"SELECT .* ['\"].*\+"),
            ("Command Injection", r"os\.system|subprocess"),
            ("XSS", r"render_template_string|innerHTML"),
            ("Code Injection", r"eval\(|exec\("),
            ("Hardcoded Secret", r"password\s*=\s*['\"]")
        ]

        for vuln, pattern in checks:
            if re.search(pattern, line):
                findings.append({
                    "type": vuln,
                    "severity": calculate_severity(vuln),
                    "line": i,
                    "code": line.strip()
                })

    return findings
