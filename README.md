
# MindMate AI (Starter)

A minimal starter for the **MindMate** project (Youth Coders Hack 2025). This is only the scaffolding for Day 1.

## Folder Structure
```
mindmate-ai/
├── backend/          # backend code (AI + APIs will live here)
│   └── app.py        # placeholder for now
├── frontend/         # frontend code will be added later
│   └── (empty)
└── README.md
```

## Day 1 — What to do next
1) Initialize git and make the first commit.
2) Create a GitHub repo and push this folder.

### Git (PowerShell on Windows)
```powershell
cd mindmate-ai
git init
git branch -M main
git add .
git commit -m "chore: init MindMate repo with basic structure"
```

### Create GitHub repo (via website)
- Go to GitHub → New repository → Name: `mindmate-ai` → Public → Create.
- Copy the "…or push an existing repository" commands. They usually look like:
```powershell
git remote add origin https://github.com/<your-username>/mindmate-ai.git
git push -u origin main
```

### Optional: GitHub CLI (if installed)
```powershell
gh repo create <your-username>/mindmate-ai --public --source . --remote origin --push
```

## Next step
- Day 2 will add a real backend with sentiment analysis, then a simple UI.
