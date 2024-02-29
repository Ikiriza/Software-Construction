class Calculator:
    """A simple calculator class."""
    
    @staticmethod
    def add(x, y):
        """Add two numbers."""
        return x + y
    
    @staticmethod
    def subtract(x, y):
        """Subtract two numbers."""
        return x - y
    
    @staticmethod
    def multiply(x, y):
        """Multiply two numbers."""
        return x * y
    
    @staticmethod
    def divide(x, y):
        """
        Divide two numbers.
        
        Return None if division by zero.
        """
        if y == 0:
            return None
        return x / y
    
    @staticmethod
    def power(x, y):
        """Calculate x raised to the power of y."""
        return x ** y
    
    @staticmethod
    def absolute_value(x):
        """Return the absolute value of x."""
        return abs(x)
    
    @staticmethod
    def square_root(x):
        """Calculate the square root of x."""
        return x ** 0.5
