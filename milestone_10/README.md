№ Milestone 10 “Ancient, Inc. 3”

Everybody likes the new employee system in [Ancient, Inc.](milestone_7) developed by you, but users started occasionally spotting bugs, like the incorrect amount of birthdays on a particular month or 500 status codes returned instead of the JSON report.

You are very surprised, since the last time you deployed the code, it was working fine. It turned out that Ancient, Inc. hired another developer for another digitalization project. They were making small changes and redeploying the app from time to time, which caused the issues.

You realize that your code is missing proper testing, which could have prevented the other people from breaking the app, and you decide to fix it.

Write unit tests for your web server, for example:

- Tests for successful case
- Tests for incorrect inputs
- Tests for reading corrupted CSV file

To make testing easier, separate logic into functions that can easily be unit-tested.

> [!Tip]
> If you feel adventurous, you can refer to Flask [testing documentation](https://flask.palletsprojects.com/en/2.0.x/testing/]), and write integration tests with `pytest` as in examples.

