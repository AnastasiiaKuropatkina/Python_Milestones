import requests
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(description="Fetch reports for a specified department and month.")
    parser.add_argument("month", help="Month for which to fetch the report, e.g., 'April'.")
    parser.add_argument("department", help="Department to fetch the report for, e.g., 'Engineering'.")
    return parser.parse_args()


def fetch_report(month, department):
    url = f"http://localhost:5000/{month.lower()}?department={department}"
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
    fetch_report(args.month, args.department)