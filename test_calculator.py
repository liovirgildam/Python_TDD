import unittest
import calculator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    result = calculator.add(10,5)
    self.assertEqual(result,15)

  if __name__ == '__main__':
    unittest.main()