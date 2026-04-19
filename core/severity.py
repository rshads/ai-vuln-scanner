def calculate_severity(vuln_type):
    critical = ["Command Injection", "Code Injection"]
    high = ["SQL Injection", "XSS"]
    medium = ["Hardcoded Secret"]

    if vuln_type in critical:
        return "CRITICAL"
    elif vuln_type in high:
        return "HIGH"
    elif vuln_type in medium:
        return "MEDIUM"
    return "LOW"
