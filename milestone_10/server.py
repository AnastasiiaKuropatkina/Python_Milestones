from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)


filename = 'database.csv'
employees = []


@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month', '')
    department = request.args.get('department', '')
    if month is None:
        return 'parameter month cannot be empty', 404
    if department is None:
        return 'parameter department cannot be empty', 404

    matching_employees = []
    for emp in employees:
        print(emp["department"] == department and month == emp["birthday_month"].lower(), emp["department"], department, emp["birthday_month"].lower(), month)
        if emp["department"] == department and month == emp["birthday_month"].lower():
            matching_employees.append({"name": emp["name"], "birthday": emp["birthday"]})

    report = {
        "total": len(matching_employees),
        "employees": matching_employees
    }

    return jsonify(report), 200


@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month', '').capitalize()
    department = request.args.get('department', '')
    if month is None:
        return 'parameter month cannot be empty', 404
    if department is None:
        return 'parameter department cannot be empty', 404

    matching_employees = []
    for emp in employees:
        if emp["department"] == department and month == emp["hiring_month"]:
            matching_employees.append({"name": emp["name"], "anniversary": emp["hiring_date"]})

    report = {
        "total": len(matching_employees),
        "employees": matching_employees
    }
    return jsonify(report), 200


def read_employee_data(filename):
    employee_data = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_data.append(row)
    return employee_data


def extract_month_names(employees):
    for employee in employees:
        # Assuming 'birthday' is the key for the employee's birthday date
        birthday_str = employee['birthday']
        birthday_obj = datetime.strptime(birthday_str, '%Y-%m-%d')
        month_name = birthday_obj.strftime('%B')
        employee['birthday_month'] = month_name
        # Assuming 'hiring' is the key for the employee's birthday date
        hiring_str = employee['hiring_date']
        hiring_obj = datetime.strptime(hiring_str, '%Y-%m-%d')
        hiring_name = hiring_obj.strftime('%B')
        employee['hiring_month'] = hiring_name


if __name__ == '__main__':
    employees = read_employee_data(filename)
    extract_month_names(employees)
    app.run(debug=True)