import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def test_addition(self):
        """Test addition functionality."""
        self.assertEqual(Calculator.add(2, 3), 5)
        # Add more test cases for addition
    
    def test_subtraction(self):
        """Test subtraction functionality."""
        self.assertEqual(Calculator.subtract(5, 3), 2)
        # Add more test cases for subtraction
    
    def test_multiplication(self):
        """Test multiplication functionality."""
        self.assertEqual(Calculator.multiply(2, 3), 6)
        # Add more test cases for multiplication
    
    def test_division(self):
        """Test division functionality."""
        self.assertEqual(Calculator.divide(6, 3), 2)
        # Add more test cases for division
    
    def test_power(self):
        """Test power functionality."""
        self.assertEqual(Calculator.power(2, 3), 8)
        # Add more test cases for power
    
    def test_absolute_value(self):
        """Test absolute value functionality."""
        self.assertEqual(Calculator.absolute_value(-5), 5)
        # Add more test cases for absolute value
    
    def test_square_root(self):
        """Test square root functionality."""
        self.assertEqual(Calculator.square_root(25), 5)
        # Add more test cases for square root

if __name__ == '__main__':
    unittest.main()
