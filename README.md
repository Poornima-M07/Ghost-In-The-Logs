# Ghost In The Logs: AI Threat Hunter

A minimalist, pastel-themed Python CLI utility built to ingest raw system logs and analyze them for advanced security anomalies using a simulated Microsoft Foundry IQ threat intelligence layer.



## Visual & Aesthetic Design
Cybersecurity tools don't have to look boring. *Ghost In The Logs* features a bespoke, **minimalist pastel pink and cool grey interface** utilizing ANSI escape sequences, delivering a clean terminal experience for security operations center (SOC) analysts.


## Key Features
* **Interactive CLI Shell:** Run live log stream analysis seamlessly from a custom terminal workspace.
* **Dual-Mode Architecture:** Detects if cloud keys are absent and gracefully self-boots into a **Hackathon Demo Mode**—ensuring flawless execution for judges without requiring deployment configurations.
* **Automated Incident Compilation:** Processes raw Sysmon payload structures and automatically compiles an elegant `incident_report.md` on the fly.

---

## GitHub Copilot Collaboration & Innovation
This utility was co-authored alongside **GitHub Copilot Chat** to emphasize the power of AI pair-programming. Copilot accelerated development by:
1. Designing the asynchronous interactive command loop loop logic.
2. Formulating clean string-interception layers to parse local `dummy.log` strings seamlessly.
3. Architecting the sandbox simulation layer to keep live production secrets completely safe from public code commits.

---

## Project Blueprint
* `app.py` — The core CLI engine containing structural shell logic and aesthetics.
* `dummy.log` — A custom, pre-packaged Sysmon telemetry log containing hidden exploit markers for immediate verification testing.
* `incident_report.md` — The parsed markdown document generated automatically post-hunt session.

---

## Step-by-Step Setup & Evaluation

### 1. Prerequisites
Ensure you have Python installed on your device, then grab the essential networking libraries:
```bash
pip install requests python-dotenv
```

### 2. Launch the Secure Environment
Fire up the terminal interface:
```bash
python app.py
```

3. Run the Evaluation Command
Inside the pastel shell interface, hunt the hidden security incident inside the mock telemetry file:

```bash
analyze dummy.log
```

