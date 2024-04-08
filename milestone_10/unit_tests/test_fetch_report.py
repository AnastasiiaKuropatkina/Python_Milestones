import sys
import os
import requests
import unittest
from unittest.mock import patch
from argparse import Namespace
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetch_report import parse_arguments, fetch_report


class TestFetchReport(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_args):
        mock_args.return_value = Namespace(event='birthdays', month='April', department='HR')
        args = parse_arguments()
        self.assertEqual(args.event, 'birthdays')
        self.assertEqual(args.month, 'April')
        self.assertEqual(args.department, 'HR')

    @patch('requests.get')
    def test_fetch_report(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'{"total": 5, "employees": [{"birthday": "1990-04-01", "name": "John Doe"}]}'
        mock_get.return_value = mock_response

        fetch_report('birthdays', 'April', 'HR')

        mock_get.assert_called_once_with('http://localhost:5000/birthdays?month=april&department=HR')


if __name__ == '__main__':
    unittest.main()