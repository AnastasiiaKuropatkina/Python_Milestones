# Milestone 5 “Ancient, Inc.”

You are hired as a developer to help Ancient, Inc. digitalize. They don't have any computer system to store information about their employees - everything is basically on paper in an archive!

The last drop was the new proposal of the HR department to celebrate birthdays and hiring anniversaries of employees and give them presents. To save money, they were going to buy all the presents for the month one time with a discount. But with the current system, someone must go over the whole archive to prepare the report about how many presents need to be bought.

Your first task as a developer is to automate this process.

## Part 1 - data generation

Company employee data is not to play around with! To develop and test our program, we need first to generate synthetic data. Create a program `generate_data.py`, and write data to `database.csv` file. You can generate arbitrary information about employees, but be sure to include name, hiring date, department, and birthday

> [!Hint]
> To make data realistic you can either predefine the pool of names, and use `random` module, or use the Faker package (you need to install it with `pip install Faker`, feel free to ask questions in Slack as we cover the topic of 3rd party packages later in the course).

## Part 2 - report

Write a program `report.py` that will take as arguments the database file name and month and will print the search result.

```bash
python report.py database.csv april
Report for April generated
--- Birthdays ---
Total: 45
By department:
- HR: 10
- Finance: 15
- Engineering: 20
--- Anniversaries ---
Total: 31
By department:
- Finance: 5
- R&D: 10
- Engineering: 16
```

Optionally, implement `-v` (verbose) flag, which will also add employee names to the report.

Compress `generate_data.py`, `report.py`, and `database.csv` files to `<surname>_5.zip` and upload it to CMS.
