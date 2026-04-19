
---

### 6️⃣ إنشاء ملف `example_vulnerable_code.py`

```bash
cat > example_vulnerable_code.py << 'EOF'
import sqlite3
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

# SQL Injection vulnerability
@app.route("/login")
def login():
    user = request.args.get("username")
    password = request.args.get("password")
    # Insecure: user input directly in the SQL query
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(query)  # ❌ Vulnerable
    return "Logged in"

# Cross-Site Scripting (XSS) vulnerability
@app.route("/profile")
def profile():
    username = request.args.get("user")
    # Insecure: user input rendered unescaped
    html = f"<h2>Welcome, {username}!</h2>"
    return render_template_string(html)  # ❌ Vulnerable

# Insecure subprocess usage
@app.route("/ping")
def ping():
    host = request.args.get("host")
    # Insecure: user input in subprocess
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return output
EOF
