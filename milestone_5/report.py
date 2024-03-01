import csv
from argparse import ArgumentParser
from datetime import datetime
from collections import defaultdict


def parse_arguments():
    parser = ArgumentParser(description="Generate a report from an employee database.")
    parser.add_argument("database", help="The CSV database file name.")
    parser.add_argument("month", help="The month to generate the report for.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Include employee names in the report.")
    return parser.parse_args()


def read_database(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def generate_report(database, month, verbose):
    birthdays = defaultdict(list)
    anniversaries = defaultdict(list)
    month_number = datetime.strptime(month, "%B").month

    for row in database:
        birthday_month = datetime.strptime(row['birthday'], "%Y-%m-%d").month
        hiring_month = datetime.strptime(row['hiring_date'], "%Y-%m-%d").month

        if birthday_month == month_number:
            birthdays[row['department']].append(row['name'])
        if hiring_month == month_number:
            anniversaries[row['department']].append(row['name'])
    
    print(f"Report for {month} generated")
    print_report("Birthdays", birthdays, verbose)
    print_report("Anniversaries", anniversaries, verbose)


def print_report(title, data, verbose):
    print(f"--- {title} ---")
    total = sum(len(names) for names in data.values())
    print(f"Total: {total}")
    print("By department:")
    for department, names in data.items():

        print(f"- {department}: {len(names)}")
        if verbose:
            for name in names:
                print(f"  {name}")


if __name__ == "__main__":
    args = parse_arguments()
    database = read_database(args.database)
    generate_report(database, args.month.capitalize(), args.verbose)