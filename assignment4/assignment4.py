# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

from pathlib import Path

import pandas as pd

_here = Path(__file__).resolve().parent

# Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a new column (separate object so task1_data_frame stays as in the spec/tests):
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# Copy of task1_with_salary with Age incremented by 1:
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# Save the DataFrame as a CSV file (next to this script so paths work from any CWD):
employees_path = _here / "employees.csv"
employees_csv = task1_older.to_csv(employees_path, index=False)
print(employees_csv)


# Task 2: Loading Data from CSV and JSON

# Read data from a CSV file:
task2_employees = pd.read_csv(employees_path)
print(task2_employees)

# Read data from a JSON file:
json_employees = pd.read_json(_here / "additional_employees.json")
print(json_employees)

# Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Using the head() method:
first_three = more_employees.head(3)
print(first_three)

# Using the tail() method:
last_two = more_employees.tail(2)
print(last_two)

# Get the shape of a DataFrame:
employee_shape = more_employees.shape
print(employee_shape)

# Use the info() method:
print(more_employees.info())


# Task 4: Data Cleaning

# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data:
dirty_data = pd.read_csv(_here / "dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame:
clean_data = clean_data.drop_duplicates()
print(clean_data)

# Convert the Age to numeric and handle missing values:
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data['Age'])

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN:
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
print(clean_data['Salary'])

# Fill missing numeric values (use fillna). Fill Age which the mean and Salary with the median:
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data['Age'])
print(clean_data['Salary'])

# Convert Hire Date to datetime (mixed formats in one column, e.g. 2021/01/15 vs 3/25/2019):
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"], format="mixed", errors="coerce"
)
print(clean_data['Hire Date'])

# Strip extra whitespace and standardize Name and Department as uppercase:
clean_data['Name'] = clean_data['Name'].str.strip().str.title()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data['Name'])
print(clean_data['Department'])
