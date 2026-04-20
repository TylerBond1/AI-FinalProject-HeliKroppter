import pandas as pd

df = pd.read_excel("inData.xlsx")
print(df.head()) # Input data

df = df.set_index(df.columns[0])  # makes student names the index
availability = 1 - df
availability = availability.drop(columns=['M10', 'W10', 'F10'])

print(availability.head()) # Modified input data optimized for deciding office hours