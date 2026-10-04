# 📬 Python Cold Outreach Automation

A lightweight, beginner-friendly Python script built to automate personal cold email outreach using standard SMTP over SSL.

---

## 🎯 Features
- Reads recipient lists directly from a plain text file (`leads.txt`).
- Connects securely to Gmail SMTP on port 465.
- Applies randomized delays (5–10s) between dispatches to maintain reasonable sending rates.
- Keeps private credentials fully decoupled from the codebase using environment variables.

---

## ⚙ Setup & Usage

### 1. Set Credentials
Configure your Gmail credentials in your environment:

```bash
export GMAIL_USER="your-email@example.com"
export GMAIL_APP_PASSWORD="your-16-char-app-password"
