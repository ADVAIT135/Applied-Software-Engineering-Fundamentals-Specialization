# 📊 Simple Interest Calculator Project

## 📌 Introduction
This project demonstrates how to host a **Simple Interest Calculator** on GitHub while following open‑source best practices.  
It was developed as part of the IBM Skills Network labs to practice GitHub UI and Git CLI workflows.

The calculator computes simple interest given:
- **p**: principal amount  
- **t**: time period in years  
- **r**: annual rate of interest  

Formula:  simple interest = (p * t * r) / 100


---

## 🎯 Objectives
By completing this project, you will:
1. Create and configure a GitHub repository.
2. Add a README, LICENSE, Code of Conduct, and Contribution Guidelines.
3. Host and commit the `simple-interest.sh` script.
4. Practice Git CLI commands: branching, merging, reverting, and pull requests.
5. Demonstrate collaboration workflows with forks and upstream repositories.

---

## 🔗 Repository Links
- **Main Repository**: [github-final-project](https://github.com/ADVAIT135/github-final-project.git)  
- **README.md**: [View README](https://github.com/ADVAIT135/github-final-project/blob/main/README.md)  
- **Apache License 2.0**: [LICENSE](https://github.com/ADVAIT135/github-final-project/blob/main/LICENSE)  
- **Code of Conduct**: [CODE_OF_CONDUCT.md](https://github.com/ADVAIT135/github-final-project/blob/main/CODE_OF_CONDUCT.md)  
- **Contribution Guidelines**: [CONTRIBUTING.md](https://github.com/ADVAIT135/github-final-project/blob/main/CONTRIBUTING.md)  
- **Simple Interest Script**: [simple-interest.sh](https://github.com/ADVAIT135/github-final-project/blob/main/simple-interest.sh)  

---

## ⚙️ Setup Instructions
Clone the repository and run the script locally:

```bash
# Clone the repo
git clone https://github.com/ADVAIT135/github-final-project.git
cd github-final-project

# Configure Git (replace with your details)
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"

# Run the calculator
bash simple-interest.sh
```
---
# 🧰 Git Commands Reference

| Command              | Description                                                                 | Example                                      |
|----------------------|-----------------------------------------------------------------------------|----------------------------------------------|
| `git init`           | Initialize a new repository                                                 | `git init myrepo`                            |
| `git clone`          | Clone a remote repository                                                   | `git clone <repo-url>`                       |
| `git branch`         | List, create, or delete branches                                            | `git branch bug-fix-typo`                    |
| `git checkout`       | Switch branches                                                            | `git checkout main`                          |
| `git switch`         | Alternative to checkout for switching/creating branches                     | `git switch <branch-name>`                   |
| `git add`            | Stage changes                                                              | `git add .`                                  |
| `git commit`         | Commit staged changes                                                      | `git commit -m "message"`                    |
| `git status`         | Show working directory and staging status                                   | `git status`                                 |
| `git log`            | View commit history                                                        | `git log -p filename`                        |
| `git diff`           | Show differences between commits or working directory                       | `git diff HEAD~1 HEAD`                       |
| `git merge`          | Merge a branch into the current branch                                      | `git merge bug-fix-typo`                     |
| `git revert`         | Undo a commit by creating a new commit                                      | `git revert HEAD`                            |
| `git reset`          | Undo changes in staging/working directory                                   | `git reset HEAD~1`                           |
| `git restore`        | Discard or reset changes in files                                           | `git restore <file>`                         |
| `git fetch`          | Download changes from remote without merging                                | `git fetch origin main`                      |
| `git pull`           | Fetch and merge changes from remote                                         | `git pull origin main`                       |
| `git push`           | Push local commits to remote repository                                     | `git push origin main`                       |
| `git remote`         | Manage remote repositories                                                 | `git remote add upstream https://github.com/original/repo.git` |
| `git remote -v`      | View remotes associated with the repository                                 | `git remote -v`                              |
| `git remote rename`  | Rename a remote repository                                                  | `git remote rename origin upstream`          |
| `git remote rm`      | Remove a remote repository                                                  | `git remote rm origin`                       |
| `git config`         | Set user configuration (email, name, defaults)                              | `git config --global user.email "you@example.com"` |
| `git version`        | Display installed Git version                                               | `git --version`                              |
| `git request-pull`   | Generate a summary of changes for upstream                                  | `git request-pull origin/main your-branch`   |
| `git format-patch`   | Generate patches for email submission                                       | `git format-patch -n 3`                      |
| `git send-email`     | Send patches via email                                                      | `git send-email --to=recipient@example.com *.patch` |
| `git am`             | Apply patches to repository                                                 | `git am <patchfile.patch>`                   |
| `git daemon`         | Expose repositories via Git protocol                                        | `git daemon --reuseaddr --verbose`           |
| `git instaweb`       | Launch a web interface for browsing repositories                            | `git instaweb -p 8080`                       |
| `git rerere`         | Reuse recorded resolutions of merge conflicts                               | `git rerere`                                 |

---

📌 **Tip:** Use `git checkout -b <branch-name>` to create and switch to a new branch in one step.  
⚠️ **Warning:** Commands like `git reset --hard HEAD` permanently discard changes — use with caution.



#### 🤝 Contribution Guidelines
All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

