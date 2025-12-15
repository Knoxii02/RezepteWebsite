import subprocess
import sys
import shutil
from pathlib import Path
import re


def clone_repo(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = Path(f"./scanned_repos/{repo_name}")
    
    if repo_path.exists():
        try:
            shutil.rmtree(repo_path)
        except PermissionError:
            print(f"Konnte {repo_path} nicht löschen (Zugriff verweigert). Überspringe...")
            return None
    
    repo_path.parent.mkdir(exist_ok=True)
    
    result = subprocess.run(['git', 'clone', repo_url, str(repo_path)], 
                          capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Fehler beim Clonen: {result.stderr}")
        return None
    
    return repo_path


def run_bandit(repo_path):
    print("\n=== BANDIT SCAN ===")
    result = subprocess.run(['bandit', '-r', str(repo_path)], 
                          capture_output=True, text=True)
    print(result.stdout)


def scan_secrets(repo_path):
    print("\n=== SECRET SCAN ===")
    
    patterns = {
        'password': r'(?i)(password|passwd|pwd)\s*[=:]\s*["\']([^"\']+)["\']',
        'api_key': r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']([^"\']+)["\']',
        'secret': r'(?i)(secret|token)\s*[=:]\s*["\']([^"\']+)["\']',
        'database': r'(?i)(mysql|postgres|mongodb)://([^:]+):([^@]+)@',
    }
    
    for py_file in repo_path.rglob('*.py'):
        try:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            
            for secret_type, pattern in patterns.items():
                for match in re.finditer(pattern, content):
                    print(f"\n[{secret_type.upper()}] {py_file.relative_to(repo_path)}")
                    print(f"  {match.group(0)}")
        except:
            pass


def main():
    if len(sys.argv) > 1:
        repo_url = sys.argv[1]
    else:
        repo_url = input("GitHub URL: ").strip()
    
    if not repo_url:
        print("Keine URL angegeben!")
        return
    
    print(f"Scanne: {repo_url}\n")
    
    repo_path = clone_repo(repo_url)
    if not repo_path:
        return
    
    run_bandit(repo_path)
    scan_secrets(repo_path)
    
    print(f"\nFertig! Repo: {repo_path}")


if __name__ == "__main__":
    main()
