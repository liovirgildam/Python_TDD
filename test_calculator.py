import unittest
import calculator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    """
    result = calculator.add(10,5)
    self.assertEqual(result,15)
    """
    self.assertEqual(calculator.add(10,5),15)
    self.assertEqual(calculator.add(-1,1),0)
    self.assertEqual(calculator.add(-1,-5),-6)
    
  def test_subtract(self):
   
    self.assertEqual(calculator.subtract(1,-1), 2)
    self.assertEqual(calculator.subtract(10,1),9)
    self.assertEqual(calculator.subtract(-1,1),-2)

  def test_multiply(self):
    self.assertEqual(calculator.multiply(1,10),10)
    self.assertEqual(calculator.multiply(2,5), 10)
    self.assertEqual(calculator.multiply(2,2),4)

  def test_divide(self):
    self.assertEqual(calculator.divide(4,2),2)
    self.assertEqual(calculator.divide(10,2.5), 4)
    self.assertEqual(calculator.divide(11,1),11)

if __name__ == '__main__':
  unittest.main()