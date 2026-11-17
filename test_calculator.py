import unittest
from calculator import *

#https://github.com/DevikaPramod2907/lab11--DP---PA-.git

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertTrue(add(3,3), 6)
        self.assertFalse(add(10, 5), 10)
        self.assertTrue(add(-1, -2), -3)


    def test_subtract(self): # 3 assertions
    #     fill in code
        self.assertTrue(subtract(20, 10), 10)
        self.assertFalse(subtract(-30, 20), -10)
        self.assertTrue(subtract(100, 100), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        self.assertRaises(div(0,5), ZeroDivisionError)

    # def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(8,2), 3)
        self.assertEqual(log(9, 3), 2)
        self.assertEqual(log(1000,10), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        self.assertRaises(div(10, 1), ValueError)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()