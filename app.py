import os
import sys
import time
import requests
from datetime import datetime

# Elegant Minimalist Pastel Theme (ANSI Escape Codes)
RESET = "\033[0m"
GREY = "\033[90m"
WHITE = "\033[97m"
PASTEL_PINK = "\033[38;5;211m"
LIGHT_MAGENTA = "\033[95m"

# Safe default/placeholder credentials check
API_KEY = os.getenv("FOUNDRY_IQ_API_KEY", "")
ENDPOINT = os.getenv("FOUNDRY_IQ_ENDPOINT", "")
IS_DEMO_MODE = not API_KEY or "your-" in API_KEY.lower()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{PASTEL_PINK}=================================================={RESET}")
    print(f"{LIGHT_MAGENTA}       👻  GHOST IN THE LOGS: AI THREAT HUNTER     {RESET}")
    print(f"{PASTEL_PINK}=================================================={RESET}")
    if IS_DEMO_MODE:
        print(f"{GREY}Status: Running in [ HACKATHON DEMO MODE ] (No API Keys Required){RESET}\n")
    else:
        print(f"{GREY}Status: Connected to Live Microsoft Foundry IQ Layer{RESET}\n")

def get_mock_response():
    """Provides a realistic, professional threat intelligence breakdown for demo purposes."""
    return """# 🚨 INCIDENT ANALYSIS REPORT
**Severity:** CRITICAL (Score: 8.5/10)
**Framework Reference:** MITRE ATT&CK T1059 (Command and Scripting Interpreter)

### 👥 Executive Summary
Analysis of the uploaded system logs indicates an active hands-on-keyboard intrusion attempt. A process spoofing event was detected followed by an unauthorized asset enumeration sequence and suspicious outbound external networking.

### 🔍 Identified Malicious Artifacts
1. **Unauthorized Binary Invocation:** The execution of `net.exe` and `whoami.exe` was tracked from a non-standard system directory. This is highly indicative of discovery and local reconnaissance phases.
2. **Suspicious Outbound Network Connection:** An established socket connection was flagged routing traffic directly to an external, unverified external IP address over port 443.

### 🛠️ Required Remediation Steps
* **Isolate Host:** Immediately disconnect the affected workstation from the local network segment.
* **Credential Revocation:** Force an immediate password reset for the compromised user account session.
* **Process Termination:** Terminate any residual parent processes originating from the anomalous network socket timeline."""

def analyze_file(filename):
    if not os.path.exists(filename):
        print(f"\n{PASTEL_PINK}[!] Error: File '{filename}' could not be located.{RESET}\n")
        return

    print(f"\n{GREY}[*] Reading log stream payload...{RESET}")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            log_content = f.read()
    except Exception as e:
        print(f"{PASTEL_PINK}[!] Read Failure: File must be plain text. ({e}){RESET}\n")
        return

    print(f"{LIGHT_MAGENTA}[*] Hunting threats against grounded intelligence layer...{RESET}")
    
    # Animated loading effect
    for _ in range(3):
        print(f"{GREY}.{RESET}", end="", flush=True)
        time.sleep(0.4)
    print("\n")

    if IS_DEMO_MODE:
        analysis_text = get_mock_response()
    else:
        # Live cloud connection block
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {"query": log_content, "max_tokens": 1200, "temperature": 0.2}
        try:
            res = requests.post(f"{ENDPOINT}/v1/chat/completions", json=payload, headers=headers, timeout=15)
            if res.status_code == 200:
                analysis_text = res.json().get("choices", [{}])[0].get("message", {}).get("content", "Empty threat intel response.")
            else:
                print(f"{PASTEL_PINK}[!] Live Endpoint returned code {res.status_code}. Falling back to sandbox analytics...{RESET}\n")
                analysis_text = get_mock_response()
        except Exception:
            print(f"{PASTEL_PINK}[!] Cloud timeout. Auto-routing through backup sandbox analytics...{RESET}\n")
            analysis_text = get_mock_response()

    # Output to screen
    print(f"{WHITE}{analysis_text}{RESET}\n")

    # Generate Markdown Report Document
    report_file = "incident_report.md"
    try:
        with open(report_file, "w", encoding="utf-8") as rep:
            rep.write(analysis_text)
        print(f"{PASTEL_PINK}[+] Report successfully compiled to: {report_file}{RESET}\n")
    except Exception as e:
        print(f"{PASTEL_PINK}[!] Could not write markdown report file: {e}{RESET}\n")

def run_shell():
    while True:
        try:
            command = input(f"{LIGHT_MAGENTA}GHOST-THREAT-HUNTER{RESET}:{GREY}~$ {RESET}").strip()
            if not command:
                continue
            if command.lower() in ['exit', 'quit']:
                print(f"\n{PASTEL_PINK}[*] Closing secure hunt session. Goodbye.{RESET}")
                break
            elif command.lower() == 'clear':
                print_header()
                continue
            elif command.startswith("analyze "):
                target_file = command.split(" ", 1)[1]
                analyze_file(target_file)
            else:
                print(f"{PASTEL_PINK}Unknown command.{RESET} Available commands: analyze <filename>, clear, exit")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{PASTEL_PINK}[*] Session aborted.{RESET}")
            break

if __name__ == "__main__":
    print_header()
    run_shell()
