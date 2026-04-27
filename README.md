# Office Hours Scheduler Optimization

## Overview

This project is a Python-based scheduling tool designed to determine optimal office hour times for a professor. Given class schedules for a group of students who all share a common course at **10:00 AM on Monday, Wednesday, and Friday**, the program analyzes availability and recommends office hour time slots that maximize student attendance.

The goal is to minimize scheduling conflicts and provide time options that work for the largest number of students.

---

## Features

* Parses and processes multiple student schedules
* Identifies conflicts across time blocks
* Computes student availability outside scheduled classes
* Ranks and selects optimal office hour time slots
* Outputs recommended office hours based on maximum availability
* Supports professor-defined unavailable time slots via input data
* Outputs total percentage of students able to attend selected office hours

---

## How It Works

1. Student schedules are read from an input file
2. Each schedule is converted into structured time blocks
3. The program determines when students are **not** in class
4. Candidate office hour time slots are evaluated
5. Time slots are ranked based on how many students are available
6. The top results are returned as recommended office hours
7. Applies constraints such as fixed class times and instructor unavailability before optimization

---

## Input Format

The program expects an input file containing schedules for 20 students.

Each student’s schedule should include:

* Days of the week (`M`, `T`, `W`, `R`, `F`)
* Time ranges for each class

### Example Input

```
Student1:
MWF 9:00-10:00
TR 1:00-2:30

Student2:
MWF 11:00-12:00
TR 9:30-10:45
```

---

## Output Format

The program outputs a list of recommended office hour time slots along with the percent of students available.

### Example Output

```
Optimal Office Hours:
- M14
- W15

Coverage: 85.0% of students (17/20)
```

---

## Installation

1. Clone this repository:

   ```
   git clone <https://github.com/c-dusek/AI-FinalProject-HeliKroppter.git>
   cd <https://github.com/c-dusek/AI-FinalProject-HeliKroppter.git>
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   **Mac/Linux:**

   ```
   source venv/bin/activate
   ```

   **Windows:**

   ```
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

---

## Usage

Run the program with:

```
python main.py inData.txt
```
---

## Dependencies

* Python 3.x
* pandas
---

## Assumptions & Limitations

* Designed for a fixed group of **20 students**
* Assumes all students share a class at **10:00 AM MWF**
* Only considers availability (not personal preferences)
* Time resolution depends on how schedules are defined in the input
* Time slots must match between student data and professor constraints
* Input data must be formatted correctly in Excel

---

## Customization
Users can modify:
- Number of office hours selected
- Professor unavailable times (via Excel input)
- Student schedule data

---

## Future Improvements

* Support variable number of students
* Add a graphical user interface (GUI)
* Incorporate student preferences or weighting
* Export results to calendar formats (Google Calendar, Outlook, etc.)
* Improve optimization algorithm for larger datasets

---

## License

This project is intended for educational use.

---
