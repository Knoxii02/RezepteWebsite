# GitHub Repository Scanner - Anleitung

## 📋 Installation

```powershell
pip install -r scanner_requirements.txt
```

## 🚀 Verwendung

### Methode 1: Mit Command Line Argument

```powershell
python github_scanner.py https://github.com/username/repo.git
```

### Methode 2: Interaktiv

```powershell
python github_scanner.py
# Gibt dann URL ein wenn gefragt
```

## 📊 Beispiel-URLs zum Testen

```powershell
# Dein eigenes Repo
python github_scanner.py https://github.com/Knoxii02/RezepteWebsite.git

# Andere Repos (Beispiele - ersetze mit echten URLs deiner Kommilitonen)
python github_scanner.py https://github.com/student1/hacking-project.git
python github_scanner.py https://github.com/student2/flask-security.git
python github_scanner.py https://github.com/student3/python-webapp.git
python github_scanner.py https://github.com/student4/security-demo.git
python github_scanner.py https://github.com/student5/web-hacking.git
```

## 🔍 Was wird gescannt?

✅ **Bandit:** Python Security Issues

- SQL Injection
- Hardcoded Passwords
- eval() usage
- Shell Injection
- etc.

✅ **Secret Scanner:** Passwörter & API-Keys

- password = "..."
- api_key = "..."
- Database Connection Strings
- AWS Keys
- Tokens & Secrets

## 📁 Output

Nach dem Scan findest du:

```
scanned_repos/
├── username_repo/              # Geclontes Repository
├── username_repo_report.json   # JSON Report
└── username_repo_report.html   # HTML Report (im Browser öffnen!)
```

## 🎯 Workflow

1. **Installiere Dependencies:**

   ```powershell
   pip install bandit
   ```

2. **Scanne 5 Repos:**

   ```powershell
   python github_scanner.py https://github.com/user1/repo1.git
   python github_scanner.py https://github.com/user2/repo2.git
   python github_scanner.py https://github.com/user3/repo3.git
   python github_scanner.py https://github.com/user4/repo4.git
   python github_scanner.py https://github.com/user5/repo5.git
   ```

3. **Öffne HTML-Reports** in deinem Browser

4. **Dokumentiere Findings** für deine Abgabe

## 📊 Report-Inhalt

Der HTML-Report zeigt:

- Anzahl gefundener Issues
- Severity-Level (CRITICAL, HIGH, MEDIUM, LOW)
- Dateiname und Zeilennummer
- Code-Snippet
- Gefundene Passwörter/Secrets

## ⚠️ Wichtig

- Git muss installiert sein!
- Bandit muss installiert sein: `pip install bandit`
- Du brauchst Zugriff auf die GitHub-Repos (public oder mit deinem Account)
