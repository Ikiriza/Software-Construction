# Core framework for Employee management and reporting

from abc import ABC, abstractmethod

# Base class for all types of employees, enforcing implementation of specific functionalities
class Employee(ABC):
    def __init__(self, name):
        """Initialize with employee name."""
        self.name = name

    @abstractmethod
    def get_bonus(self):
        """Defines how to compute bonus; must be overridden."""
        pass

    @abstractmethod
    def get_report(self):
        """Defines how to generate report; must be overridden."""
        pass

# Derived class for managers with specialized implementations
class Manager(Employee):
    def get_bonus(self):
        """Calculates bonus for Managers."""
        return 1000

    def get_report(self):
        """Generates report specific to Managers."""
        return f"Manager Report: {self.name}"

    def manage_team(self):
        """Executes management-specific tasks."""
        print(f"{self.name} is managing the team.")

# Derived class for developers with specialized implementations
class Developer(Employee):
    def get_bonus(self):
        """Calculates bonus for Developers."""
        return 500

    def get_report(self):
        """Generates report specific to Developers."""
        return f"Developer Report: {self.name}"

    def code_review(self):
        """Executes developer-specific tasks."""
        print(f"{self.name} is conducting a code review.")

# Utility class for calculating bonuses for any Employee type
class BonusCalculator:
    def calculate_bonus(self, employee: Employee):
        """Leverages Employee's implementation to calculate bonus."""
        return employee.get_bonus()

# Utility class for generating reports for any Employee type
class ReportGenerator:
    def generate_report(self, employee: Employee):
        """Utilizes Employee's method to generate and print a report."""
        print(employee.get_report())

# Application entry point demonstrating usage of classes
if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    # Generating and printing reports for both Manager and Developer
    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    # Calculating and displaying bonuses
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    # Demonstrating role-specific behaviors
    manager.manage_team()
    developer.code_review()

# Unit testing the Employee management system

import unittest
from io import StringIO
import sys

# Test suite for validating functionality of the Employee management system
class TestElevateHR(unittest.TestCase):
    def setUp(self):
        """Captures stdout for inspection."""
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_employee_creation(self):
        """Ensures Employee instances are created with correct names."""
        manager = Manager("Alice")
        developer = Developer("Bob")
        self.assertEqual(manager.name, "Alice")
        self.assertEqual(developer.name, "Bob")

    def test_bonus_calculation(self):
        """Verifies correct bonus calculation for different Employee types."""
        manager = Manager("Alice")
        developer = Developer("Bob")
        bonus_calculator = BonusCalculator()
        self.assertEqual(bonus_calculator.calculate_bonus(manager), 1000)
        self.assertEqual(bonus_calculator.calculate_bonus(developer), 500)

    def test_report_generation(self):
        """Checks correct report generation and content."""
        manager = Manager("Alice")
        developer = Developer("Bob")
        report_generator = ReportGenerator()
        report_generator.generate_report(manager)
        self.assertIn("Manager Report: Alice", sys.stdout.getvalue())
        sys.stdout.seek(0)
        report_generator.generate_report(developer)
        self.assertIn("Developer Report: Bob", sys.stdout.getvalue())

    def test_specific_methods(self):
        """Tests execution of role-specific methods for Manager and Developer."""
        manager = Manager("Alice")
        developer = Developer("Bob")
        manager.manage_team()
        self.assertIn("Alice is managing the team.", sys.stdout.getvalue())
        sys.stdout.seek(0)
        developer.code_review()
        self.assertIn("Bob is conducting a code review.", sys.stdout.getvalue())

    def tearDown(self):
        """Restores stdout after each test."""
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()
