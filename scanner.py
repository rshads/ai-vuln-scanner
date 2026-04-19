cat > scanner.py << 'EOF'
import tempfile
import subprocess
import json
import os

VULN_PATTERNS = [
    {
        "id": "python.lang.security.injection-sqli",
        "type": "SQL Injection",
        "severity": "High"
    },
    {
        "id": "python.lang.security.injection-xss",
        "type": "Cross-Site Scripting (XSS)",
        "severity": "High"
    },
    {
        "id": "python.lang.security.injection-command",
        "type": "Command Injection",
        "severity": "High"
    },
    {
        "id": "python.lang.security.hardcoded-secret",
        "type": "Hardcoded Secret",
        "severity": "Medium"
    },
    {
        "id": "python.lang.security.dangerous-function-use",
        "type": "Unsafe Function",
        "severity": "Medium"
    }
]

def scan_code(code):
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        tmp_path = tmp.name
    results = []
    try:
        proc = subprocess.run(
            [
                "semgrep",
                "--config=auto",
                "--json",
                tmp_path
            ],
            capture_output=True,
            text=True,
            check=False
        )
        if proc.returncode not in (0, 1):
            return []
        data = json.loads(proc.stdout)
        for m in data.get("results", []):
            rule_id = m.get("check_id", "")
            vuln_info = None
            for pattern in VULN_PATTERNS:
                if pattern["id"] in rule_id:
                    vuln_info = pattern
                    break
            if not vuln_info:
                sev = m.get("extra", {}).get("severity", "Low").capitalize()
                msg = m.get("extra", {}).get("message", "").lower()
                for pattern in VULN_PATTERNS:
                    if pattern["type"].lower() in msg:
                        vuln_info = pattern
                        break
            if not vuln_info:
                vuln_info = {
                    "type": m.get("extra", {}).get("message", "Unknown"),
                    "severity": m.get("extra", {}).get("severity", "Low").capitalize()
                }
            results.append({
                "type": vuln_info["type"],
                "severity": vuln_info["severity"],
                "file": os.path.basename(m["path"]),
                "line": m["start"]["line"],
                "code": m["extra"].get("lines", ""),
                "meta": m
            })
    except Exception as e:
        results = [{"type": "Scan Error", "severity": "High", "file": "", "line": "-", "code": str(e), "meta": {}}]
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
    return results
EOF
