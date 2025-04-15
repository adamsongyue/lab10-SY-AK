import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,2.1),4.2)
        self.assertEqual(mul(0,5),0)
        self.assertEqual(mul(-3,2), -6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2),1)
        self.assertEqual(div(-9,3),-3)
        self.assertEqual(div(9,2),4.5)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
          with self.assertRaises(ValueError):
              logarithm(1, 3)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,0),5)
        self.assertAlmostEqual(hypotenuse(-3,6.5),7.158910531638177)

    def test_sqrt(self): # 3 assertions
          # Test for invalid argument, example:
         with self.assertRaises(ValueError):
             square_root(-4)
         self.assertAlmostEqual((square_root(5)),2.23606797749979)
         self.assertEqual(square_root(0),0)
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()