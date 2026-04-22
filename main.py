import pandas as pd
import pulp

df = pd.read_excel("inData.xlsx")
print(df.head()) # Input data

df = df.set_index(df.columns[0])  # makes student names the index
availability = 1 - df
availability = availability.drop(columns=['M10', 'W10', 'F10'])

print(availability.head()) # Modified input data optimized for deciding office hours

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
model += pulp.lpSum([x[t] for t in times]) == 5

# Constraint: student coverage
for s in students:
    model += y[s] <= pulp.lpSum([availability.loc[s, t] * x[t] for t in times])

# Solve
model.solve()

# Results
selected_times = [t for t in times if x[t].value() == 1]
covered_students = sum(y[s].value() for s in students)

print("Selected office hours:", selected_times)
print("Students covered:", covered_students)