# 📘 Hands-On Linux & Shell Scripting Learning Resource

Welcome to the **Linux Commands and Shell Scripting** learning repository.  
This repository consolidates **cheat sheets, labs, practice projects, and final project instructions** into a single actionable resource for learners and practitioners.

---

## 📂 Contents

- [Module 1: Introduction to Linux](#module-1-introduction-to-linux)
- [Module 2: Linux Commands](#module-2-linux-commands)
- [Module 3: Shell Scripting](#module-3-shell-scripting)
- [Cumulative Cheat Sheet](#cumulative-cheat-sheet)
- [Practice Project: Weather ETL](#practice-project-weather-etl)
- [Final Project: Automated Backup Script](#final-project-automated-backup-script)


---

## Module 1: Introduction to Linux

- Navigating directories (`ls`, `pwd`, `cd`)
- Special paths (`~`, `/`, `.`, `..`)
- Package management (`sudo apt update`, `sudo apt install`)
- File creation and editing (`nano file.txt`)

👉 Refer to [Module 1 Cheat Sheet](Module%201%20Cheat%20Sheet%20.pdf) for quick commands.

---

## Module 2: Linux Commands

- System info (`whoami`, `id`, `uname -a`)
- Process management (`ps`, `top`, `df`)
- File operations (`touch`, `cp`, `mv`, `rm`)
- Permissions (`chmod u+x file.sh`)
- Text wrangling (`cat`, `head`, `tail`, `sort`, `uniq`, `wc`)
- Pattern search (`grep -iw hello file.txt`)
- Archiving (`tar`, `zip`, `unzip`)
- Networking (`hostname`, `ping`, `ip`, `curl`, `wget`)

👉 Refer to [Module 2 Cheat Sheet](Module%202%20Cheat%20Sheet.pdf).

---

## Module 3: Shell Scripting

- Shebang (`#!/bin/bash`)
- Pipes & filters (`ls | sort -r`)
- Variables (`my_var=Earth`, `echo $my_var`)
- Conditionals (`if [[ $# == 2 ]] ... fi`)
- Loops (`for i in {1..5}; do ... done`)
- Arrays (`declare -a myArray`)
- Cron jobs (`crontab -e`, `15 18 * * 0 date >> sundays.txt`)

👉 Refer to [Module 3 Cheat Sheet](Module%203%20Cheat%20Sheet%20(1).pdf).

---

## Cumulative Cheat Sheet

A consolidated reference of **Linux commands and shell scripting essentials**.  
Includes navigation, file operations, text processing, networking, and cron scheduling.

👉 See [Cumulative Cheat Sheet](Cumulative%20Cheat%20Sheet.pdf).

---

## Practice Project: Weather ETL

**Scenario:** Automate an ETL process to extract daily weather data for Casablanca using `curl wttr.in/casablanca`.  
**Tasks:**
- Extract observed and forecasted temperatures.
- Transform into tabular format.
- Load into a log file.
- Schedule with cron to run daily at noon.

👉 See [Practice Project Overview](Practice%20Project%20Overview.pdf).

---

## Final Project: Automated Backup Script

**Scenario:** Create `backup.sh` to automatically back up encrypted password files updated in the past 24 hours.  
**Tasks:**
1. Parse command-line arguments.
2. Validate directories.
3. Capture current timestamp.
4. Generate backup filename (`backup-[timestamp].tar.gz`).
5. Identify modified files in last 24 hours.
6. Archive with `tar`.
7. Move backup to destination directory.
8. Schedule with `cron` for daily execution.

👉 See [Final Project Instructions](Final%20project%20instructions.pdf) and [FINAL PROJECT.docx](FINAL%20PROJECT.docx).

---



---

## 🚀 How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/linux-shell-scripting.git
2. Navigate into the repo:
   ```bash
   cd linux-shell-scripting
3. Explore cheat sheets and labs.
4. Complete practice and final projects.
5. Use cron to automate scripts.

## 📌 Authors & Contributors
- Course Authors: Md Haroon Hussain, Rajashree Patil
- Practice Project: Jeff Grossman
- Other Contributors: Rav Ahuja, IBM Corporation

