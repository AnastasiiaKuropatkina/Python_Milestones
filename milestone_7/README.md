# Milestone 7 “Ancient, Inc. 2”

Let's return to your job at Ancient, Inc. The report tool (developed as the task for Milestone 5) was a huge success, but too much work for the HR department.

Now they want to delegate the work of congratulating the employees to the departments, but it's still their responsibility to maintain the employee database, so they want to expose report functionality via API!

## Part 1 - server

Your task is to write a simple flask server that will have the following endpoints:

- `GET /birthdays?month=april&department=HR`
- `GET /anniversaries?month=april&department=HR`

The response should be a JSON-encoded report:

```json
{
    "total": 1,
    "employees": {
        {"id": 1, "name": "John Doe", "birthday": "Apr 18"}
    }
}
```

or similar.

## Part 2 - client

To make life easier for departments, HR wants to distribute a cli-utility to query the API like this:

```bash
python fetch_report.py birthdays april HR
Report for HR department for April fetched.
Total: 4
Employees:
- 1989-04-13, Marie Small
```

or similar.

Implement `fetch_report.py` using `requests` library. To test it, run the server from Part 1 locally on port 5000.

## Local development

You need to have Python 3.10 or higher.

- Create a new virtual environment `python3 -m venv ./venv` and activate it
- Install packages `pip3 install -r requirements.txt`
- Run the code `python3 server.py`

To run linting checks locally, you may also do:

- Install linters `pip3 install flake8 mypy`
- To run code linting: `flake8 .`
- To run type checker `mypy .`
