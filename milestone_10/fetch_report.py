import requests
from argparse import ArgumentParser
import csv


def parse_arguments():
    parser = ArgumentParser(description="Fetch reports for a specified: event department month.")
    parser.add_argument("event", help="Month for which to fetch the report, e.g., 'birthdays' or 'anniversaries'.")
    parser.add_argument("month", help="Month for which to fetch the report, e.g., 'April'.")
    parser.add_argument("department", help="Department to fetch the report for, e.g., 'HR'.")
    return parser.parse_args()


def read_database(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def fetch_report(event, month, department):
    url = f"http://localhost:5000/{event.lower()}?month={month.lower()}&department={department}"
    response = requests.get(url)
    if response.status_code == 200:
        report = response.json()
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {report['total']}")
        if 'employees' in report:
            print("Employees:")
            for employee in report['employees']:
                print(f"- {employee['birthday']}, {employee['name']}")
    else:
        print("Failed to fetch report. Please ensure the server is running and the parameters are correct.")


if __name__ == "__main__":
    args = parse_arguments()
    fetch_report(args.event, args.month, args.department)