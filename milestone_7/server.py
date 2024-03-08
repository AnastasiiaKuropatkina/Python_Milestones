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
    matching_employees = [
        {"name": emp["name"], "birthday": emp["birthday"]}
        for emp in employees
        if emp["department"] == department and month == emp["birthday"].lower()
    ]

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

    matching_employees = [
        {"name": emp["name"], "anniversary": emp["anniversary"]}
        for emp in employees if emp["department"] == department and month in emp["birthday_month"].lower()
    ]

    report = {
        "total": len(matching_employees),
        "employees": matching_employees
    }
    return jsonify(report), 200

def read_employee_data(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        employee_data = [row for row in reader]
    return employee_data

def extract_month_names(employees):
    for employee in employees:
        # Assuming 'birthday' is the key for the employee's birthday date
        birthday_str = employee['birthday']
        birthday_obj = datetime.strptime(birthday_str, '%Y-%m-%d')
        month_name = birthday_obj.strftime('%B')
        employee['birthday_month'] = month_name

if __name__ == '__main__':
    employees = read_employee_data(filename)
    extract_month_names(employees)
    # for employee in employees:
    #     print(f"Name: {employee['name']}, Department: {employee['department']}, Birthday: {employee['birthday']}")

    #print("employees==>",employees)
    app.run(debug=True)