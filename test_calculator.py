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

if __name__ == '__main__':
  unittest.main()