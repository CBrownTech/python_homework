# Task 3: List Comprehensions Practice

import csv

with open("../csv/employees.csv", newline="", encoding="utf-8") as csv_file:
    rows = list(csv.reader(csv_file))

names = [f"{row[1]} {row[2]}" for row in rows[1:]]
print(names)

names_with_e = [name for name in names if "e" in name]
print(names_with_e)
