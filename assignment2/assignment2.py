# Task 2: Read a CSV file
import csv
import os
import sys
import traceback
from datetime import datetime


def read_employees():
    data = {}
    rows_list = []
    try:
        with open("../csv/employees.csv", newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows_list.append(row)
            data["rows"] = rows_list
        return data
    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)
employees = read_employees()
employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name
def first_name(row_number):
    col = column_index("first_name")
    return employees["rows"][row_number][col]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches

# Task 7: Sort the Rows by last_name Using a lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    result = dict(zip(employees["fields"], row))
    result.pop("employee_id", None)
    return result


print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        e_id = row[employee_id_column]
        result[e_id] = employee_dict(row)
    return result

print(all_employees_dict())


# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("secret-word")  
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def _read_minutes_csv(path):
    data = {}
    rows_list = []
    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows_list.append(tuple(row))
            data["rows"] = rows_list
        return data
    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)


def read_minutes():
    minutes1 = _read_minutes_csv("../csv/minutes1.csv")
    minutes2 = _read_minutes_csv("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2

minutes_set = create_minutes_set()
print(minutes_set)


# Task 14: Convert to datetime
def create_minutes_list():
    rows = list(minutes_set)
    return list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            rows,
        )
    )


# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_rows = sorted(minutes_list, key=lambda row: row[1])
    converted = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            sorted_rows,
        )
    )
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted


minutes_list = create_minutes_list()
print(minutes_list)
_sorted_minutes = write_sorted_list()
if os.access("./minutes.csv", os.F_OK):
    print("minutes.csv created OK; first sorted row:", _sorted_minutes[0])
    with open("./minutes.csv", newline="") as f:
        reader = csv.reader(f)
        file_rows = list(reader)
    if (
        len(file_rows) >= 2
        and file_rows[0] == minutes1["fields"]
        and file_rows[1][0] == "Jason Tucker"
        and file_rows[1][1] == "September 20, 1980"
    ):
        print("minutes.csv content check passed (header and first data row).")
    else:
        print("minutes.csv content unexpected:", file_rows[:3])
else:
    print("ERROR: minutes.csv was not created (check working directory).")
