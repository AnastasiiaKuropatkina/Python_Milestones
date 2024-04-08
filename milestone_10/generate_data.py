from faker import Faker
import csv


def generate_employee_data(num_employees=100):
    fake = Faker()
    employees = []

    for _ in range(num_employees):
        name = fake.name()
        hiring_date = fake.date_between(start_date='-5y', end_date='today')
        department = fake.job()
        birthday = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65)
        employees.append({"name": name, "hiring_date": hiring_date, "department": department, "birthday": birthday})

    return employees


def write_to_csv(employees, filename='database.csv'):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['name', 'hiring_date', 'department', 'birthday']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for employee in employees:
            writer.writerow(employee)


if __name__ == "__main__":
    employees = generate_employee_data(100)  # Generate data for 100 employees
    write_to_csv(employees)