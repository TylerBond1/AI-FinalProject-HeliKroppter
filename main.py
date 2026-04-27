import pandas as pd
import pulp

hours = 3 # MAKE APP INPUT

df = pd.read_excel("inData.xlsx") # FIND BETTER WAY TO INPUT INTO APP
print(df.head()) # Input data

df = df.set_index(df.columns[0])  # makes student names the index
availability = 1 - df
availability = availability.drop(columns=['M10', 'W10', 'F10'])

# Drop Professor Unavailability (Constraints)
availability = availability.drop(columns=['M8', 'M12', 'T12', 'W12','R8', 'R9', 'R10', 'R12','F8', 'F12']) # MAKE APP INPUT

# Get list of students and time slots
students = availability.index.tolist()
times = availability.columns.tolist()

# Create problem
model = pulp.LpProblem("OfficeHoursOptimization", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable.dicts("timeslot", times, cat='Binary')
y = pulp.LpVariable.dicts("student", students, cat='Binary')

# Objective: maximize covered students
model += pulp.lpSum([y[s] for s in students])

# Constraint: pick exactly 5 time slots
model += pulp.lpSum([x[t] for t in times]) == hours

# Constraint: student coverage
for s in students:
    model += y[s] <= pulp.lpSum([availability.loc[s, t] * x[t] for t in times])

# Solve
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Results
selected_times = [t for t in times if x[t].value() == 1]
covered_students = sum(y[s].value() for s in students)
total_students = len(students)
coverage_percent = (covered_students / total_students) * 100

selected_times = [t for t in times if x[t].value() == 1]
covered_students = sum(y[s].value() for s in students)

total_students = len(students)
coverage_percent = (covered_students / total_students) * 100

print("Optimal Office Hours:", selected_times)
print(f"Student Coverage: {covered_students}/{total_students} ({coverage_percent:.1f}%)")

# Find more workable algorithm to use
# README and ROBOTS file (Look at their project for reference)
# Turn into a desktop application