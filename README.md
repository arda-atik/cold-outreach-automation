# 📬 Local Business Cold Outreach Bot

A minimal Python script built to automate personalized email outreach for local business communication and lead discovery.

---

## 🎯 Purpose
Running manual client outreach alongside academic engineering studies is repetitive and inefficient. This lightweight utility:
- Reads prospective business contact addresses from a clean text list.
- Connects securely via Gmail SMTP using SSL.
- Applies randomized delay intervals (15–30s) between dispatches to maintain healthy sender reputation and avoid automated spam classification.

---

## ⚙ Setup & Usage

### 1. Configure Environment Variables
Store credentials in your local shell environment rather than hardcoding them into source files:

```bash
export GMAIL_USER="your-email@example.com"
export GMAIL_APP_PASSWORD="your-16-char-app-password"
