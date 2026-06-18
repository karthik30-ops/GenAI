# Student Grade System

A simple terminal-based Python program built for the **Gen AI Architect Program (Social Eagle)** assignment. The program takes a student's mark as input and prints the corresponding letter grade — using pure Python only, with no external frameworks or packages.

## 📋 Overview

This program asks the user to enter a mark between 0 and 100 and converts it into a letter grade based on a fixed grading scale. It runs entirely in the terminal — there is no website or app interface.

## 🎯 Grading Scale

| Mark Range  | Grade |
|-------------|-------|
| 90 – 100    | A     |
| 80 – 89     | B     |
| 70 – 79     | C     |
| 60 – 69     | D     |
| Below 60    | E     |

> Boundaries are inclusive — a mark of exactly 90 is an A, exactly 80 is a B, and so on.

## ✅ Requirements

- Python 3.x installed on your system
- No third-party packages required — uses only the Python standard library
- Works on Windows, macOS, and Linux

## 📁 Project Structure

```
grade-system/
├── venv/                 # Virtual environment (not committed to GitHub)
├── grade_system.py       # Main program file
└── README.md             # This file
```

## 🚀 Setup and Installation

Follow these steps in order to set up and run the project locally.

### Step 1 — Clone or create the project folder

```bash
git clone <your-repository-link>
cd grade-system
```

Or, if starting fresh:

```bash
mkdir grade-system
cd grade-system
```

### Step 2 — Create a virtual environment (venv)

A virtual environment keeps this project isolated from the rest of your system.

```bash
python -m venv venv
```

> On some systems, use `python3` instead of `python`.

### Step 3 — Activate the virtual environment

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

Once activated, you should see `(venv)` at the start of your terminal prompt.

### Step 4 — Run the program

```bash
python grade_system.py
```

Test it several times with different marks to confirm each grade band works correctly (e.g. try 95, 85, 72, 64, and 40).

### Step 5 — Deactivate the virtual environment when finished

```bash
deactivate
```

## 💻 Example Run

```
Enter your mark (0-100): 85
Mark: 85 -> Grade: B
```

## ⚠️ Handling Invalid Input

The program is designed not to crash on unexpected input. It validates that:

- The entered value is a valid number (rejects non-numeric input such as letters or symbols)
- The number falls within the 0–100 range (values above 100 or below 0 are flagged as invalid)

*(Add your own 2–3 sentence explanation here describing exactly how your code handles these cases — e.g. using `try/except` for non-numeric input and `if` checks for out-of-range values, and what message is shown to the user in each case.)*

## 📸 Sample Terminal Output

*(Paste or attach a screenshot here showing the program running with at least three different marks, including one edge case.)*

## 🛠️ Built With

- Python 3 (standard library only — no external dependencies)

## 📝Author

Karthik S
