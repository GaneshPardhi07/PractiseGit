# Python Web Calculator (Flask)

A simple web-based calculator built with Python and Flask. It accepts expressions with `+ - * / ^`, parentheses, and decimal points.

## 📁 Project files

- `app.py` - Flask application and calculation logic
- `templates/calculator.html` - HTML UI

## ⚙️ Prerequisites

- Python 3.8+ installed
- `pip` package manager

## 📦 Install dependencies

```bash
cd "C:\Users\Ganesh Pardhi\temp\pr_git\PractiseGit"
python -m pip install --upgrade pip
pip install flask
```

## ▶️ Run locally

```bash
cd "C:\Users\Ganesh Pardhi\temp\pr_git\PractiseGit"
python app.py
```

Open a browser at:

- http://127.0.0.1:5000

## 🧪 Usage

- Click the buttons to build an expression.
- Press `=` to calculate.
- Use `C` to clear.
- Supported operators: `+ - * /` and `^` (power via `**` conversion in code), and parentheses `(` `)`.

## 🛡️ Notes

- The expression parser uses Python `eval` in a restricted builtins environment. It performs character filtering to reduce risk.
- Do not expose this version on public production networks without hardened input validation.

## 🚫 Troubleshooting

- If page does not load: ensure Flask is installed, and `app.py` is being run from the project folder.
- On Windows, use quotes around paths with spaces.

## 🧩 Optional features to add

- Keyboard input support
- history of calculations
- memory buttons (M+, M-, MR, MC)
- proper expression parser (no `eval`)
