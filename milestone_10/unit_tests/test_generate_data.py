import unittest
from unittest.mock import patch, mock_open
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generate_data import generate_employee_data, write_to_csv


class TestGenerateData(unittest.TestCase):
    @patch('generate_data.Faker')
    def test_generate_employee_data(self, mock_faker):
        fake = mock_faker.return_value
        fake.name.return_value = 'John Doe'
        fake.date_between.return_value = '2022-01-01'
        fake.job.return_value = 'Engineer'
        fake.date_of_birth.return_value = '1990-01-01'

        employees = generate_employee_data(1)

        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]['name'], 'John Doe')
        self.assertEqual(employees[0]['hiring_date'], '2022-01-01')
        self.assertEqual(employees[0]['department'], 'Engineer')
        self.assertEqual(employees[0]['birthday'], '1990-01-01')

    @patch('builtins.open', new_callable=mock_open)
    @patch('csv.DictWriter')
    def test_write_to_csv(self, mock_dict_writer, mock_open):
        employees = [{'name': 'John Doe', 'hiring_date': '2022-01-01', 'department': 'Engineer', 'birthday': '1990-01-01'}]

        write_to_csv(employees)

        mock_open.assert_called_once_with('database.csv', mode='w', newline='')
        mock_dict_writer.assert_called_once_with(mock_open.return_value, fieldnames=['name', 'hiring_date', 'department', 'birthday'])
        mock_dict_writer.return_value.writeheader.assert_called_once()
        mock_dict_writer.return_value.writerow.assert_called_once_with(employees[0])


if __name__ == '__main__':
    unittest.main()