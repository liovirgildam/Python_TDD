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

    def test_fullname(self):
        self.assertEqual(self.employee_1.fullname, 'Lia Addai')
        self.assertEqual(self.employee_2.fullname, 'Lili Mendonca')

        self.employee_1.first = 'Serwaa'
        self.employee_2.first = 'Liovirgilda'

        self.assertEqual(self.employee_1.fullname, 'Serwaa Addai')
        self.assertEqual(self.employee_2.fullname, 'Liovirgilda Mendonca')

    def test_apply_raise(self):
        self.employee_1.apply_pay_raise()
        self.employee_2.apply_pay_raise()

        self.assertEqual(self.employee_1.pay, 52500)
        self.assertEqual(self.employee_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()