# ROBOTS.md

## Project Overview

This is a Python-based desktop application that determines optimal office hour time slots for a professor based on student schedule data.

The system reads student availability from an Excel spreadsheet and uses linear optimization to select a configurable number of office hour slots that maximize student attendance.

The application includes:

* A Python backend for optimization
* A lightweight HTML/CSS frontend
* A bridge between JavaScript and Python using a webview

---

## Tech Stack

* Language: Python (3.x)
* Core Libraries:

  * pandas → data processing (Excel schedules)
  * pulp → linear optimization solver
  * pywebview → frontend/backend bridge
  * pygame → UI sound effects
* Frontend:

  * HTML (`index.html`)
  * CSS (`styles.css`)

---

## Project Structure

```
AI-FinalProject-HeliKroppter/
│
├── main.py              # Main application + optimization logic + API bridge
├── index.html           # Frontend UI
├── styles.css           # UI styling
│
├── sound1.ogg           # UI sound effects
├── sound2.ogg
├── sound3.ogg
├── sound4.ogg
│
├── inData.xlsx          # Example input data (student schedules)
│
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project configuration
├── uv.lock              # Dependency lock file
│
├── README.md            # Human-readable documentation
├── ROBOTS.md            # AI-readable documentation (this file)
│
├── .venv/               # Virtual environment (not part of logic)
├── .gitignore
└── .python-version
```

---

## Architecture Overview

### 1. Frontend (HTML/CSS)

* `index.html` provides the user interface
* Collects:

  * Number of office hours
  * Excel file input
  * Professor unavailable times
* Communicates with Python via `pywebview`

### 2. Backend API (MainApi class)

* Acts as a bridge between JavaScript and Python
* Key method:

  * `button_pressed(input)` → main execution pipeline

### 3. Optimization Engine

Located inside `button_pressed`:

Steps:

1. Load Excel data using pandas
2. Convert schedule → availability matrix
3. Remove professor unavailable times
4. Define optimization problem using PuLP:

   * Decision variables:

     * `x[t]` → selected time slots
     * `y[s]` → whether a student is covered
   * Objective:

     * Maximize number of covered students
   * Constraints:

     * Select exactly N office hours
     * A student is covered only if at least one chosen slot is available
5. Solve using CBC solver
6. Return:

   * Selected time slots
   * Covered students
   * Total students
   * Coverage percentage

---

## Entry Point

Run the application with:

```
python main.py
```

This:

1. Initializes pygame (audio)
2. Creates a webview window
3. Loads the frontend (`index.html`)
4. Starts the app loop

---

## Data Expectations

### Excel Input

* First column: student names
* Remaining columns: time slots (e.g., M10, W14, etc.)
* Values:

  * 1 = busy
  * 0 = free

### Internal Representation

* Availability = `1 - schedule`
* Columns can be dropped based on professor constraints

---

## Key Conventions

* Time slots are string-based (e.g., `"M14"`, `"W10"`)
* Unavailable hours are passed as a comma-separated string
* Input from frontend must match `ButtonInput` dataclass exactly
* Optimization assumes binary availability (no weighting)

---

## Important Constraints / Gotchas

* Input list length MUST match `ButtonInput` fields exactly
* Excel formatting must be consistent
* Column names must match time slot naming convention
* No validation layer currently exists for malformed input
* pygame must initialize before playing sounds
* File dialog depends on pywebview window context

---

## AI-Safe Modification Guidelines

### Safe to Modify

* Optimization logic (objective, constraints)
* Input parsing and validation
* UI improvements (HTML/CSS)
* Adding new output formats
* Refactoring into modules

### Modify With Caution

* `MainApi` interface (frontend depends on it)
* Structure of returned values from `button_pressed`
* Excel parsing assumptions

### Avoid Breaking

* The connection between `index.html` and `MainApi`
* Field order in `ButtonInput`
* Time slot naming consistency

---

## Opportunities for Improvement

* Separate optimization logic into its own module
* Add input validation and error handling
* Support variable number of students
* Replace pygame with simpler audio handling (optional)
* Add test suite
* Improve cross-platform compatibility (notably Windows + pygame)
* Export results (CSV, calendar integration)

---

## Summary for AI Agents

This project is:

* A **linear optimization scheduling tool**
* With a **webview-based UI**
* Driven by **Excel input data**
* Focused on **maximizing student coverage**

Primary function to understand and extend:
→ `MainApi.button_pressed`

---
