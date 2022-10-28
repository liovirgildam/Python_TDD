import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_1 = Employee('Lia', 'Addai', 50000)
        self.employee_2 = Employee('Lili', 'Mendonca', 60000)
    
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.employee_1.email, 'Lia.Addai@email.com')
        self.assertEqual(self.employee_2.email, 'Lili.Mendonca@email.com')

        self.employee_1.first = 'Serwaa'
        self.employee_2.first = 'Liovirgilda'

        self.assertEqual(self.employee_1.email, 'Serwaa.Addai@email.com')
        self.assertEqual(self.employee_2.email, 'Liovirgilda.Mendonca@email.com')


if __name__ == '__main__':
    unittest.main()