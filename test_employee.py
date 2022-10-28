import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    # method that runs before each class 
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')
    # method that runs after each class
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    # method that runs before each test
    def setUp(self):
        print('setUp')
        self.employee_1 = Employee('Lia', 'Addai', 50000)
        self.employee_2 = Employee('Lili', 'Mendonca', 60000)
    
    # method that runs after each test
    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('Test email')
        self.assertEqual(self.employee_1.email, 'Lia.Addai@email.com')
        self.assertEqual(self.employee_2.email, 'Lili.Mendonca@email.com')

        self.employee_1.first = 'Serwaa'
        self.employee_2.first = 'Liovirgilda'

        self.assertEqual(self.employee_1.email, 'Serwaa.Addai@email.com')
        self.assertEqual(self.employee_2.email, 'Liovirgilda.Mendonca@email.com')

    def test_fullname(self):
        print('Test fullname')
        self.assertEqual(self.employee_1.fullname, 'Lia Addai')
        self.assertEqual(self.employee_2.fullname, 'Lili Mendonca')

        self.employee_1.first = 'Serwaa'
        self.employee_2.first = 'Liovirgilda'

        self.assertEqual(self.employee_1.fullname, 'Serwaa Addai')
        self.assertEqual(self.employee_2.fullname, 'Liovirgilda Mendonca')

    def test_apply_raise(self):
        print('Test apply raise')
        self.employee_1.apply_pay_raise()
        self.employee_2.apply_pay_raise()

        self.assertEqual(self.employee_1.pay, 52500)
        self.assertEqual(self.employee_2.pay, 63000)

    # Mocked Test
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.employee_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Addai/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            
            schedule = self.employee_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Mendonca/June')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()