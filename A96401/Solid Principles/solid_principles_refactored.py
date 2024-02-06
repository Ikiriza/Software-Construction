from abc import ABC, abstractmethod

# Defines an abstract class for Employees, ensuring compliance with the Interface Segregation Principle (ISP)
class Employee(ABC):
    def __init__(self, name):
        """Initializes an Employee instance with a name attribute."""
        self.name = name

    @abstractmethod
    def get_bonus(self):
        """Defines a contract for implementing bonus calculation logic for subclasses."""
        pass

    @abstractmethod
    def get_report(self):
        """Defines a contract for implementing report generation logic for subclasses."""
        pass

# Specific implementation for a Manager role, aligning with Open/Closed Principle (OCP) and Single Responsibility Principle (SRP)
class Manager(Employee):
    def get_bonus(self):
        """Returns the bonus amount for Manager role."""
        return 1000

    def get_report(self):
        """Creates a performance report specific to a Manager."""
        return f"Manager Report: {self.name}"

    def manage_team(self):
        """Executes tasks specific to managing a team."""
        print(f"{self.name} is managing the team.")

# Specific implementation for a Developer role, also adhering to OCP and SRP
class Developer(Employee):
    def get_bonus(self):
        """Determines the bonus amount for Developer role."""
        return 500

    def get_report(self):
        """Compiles a performance report for a Developer."""
        return f"Developer Report: {self.name}"

    def code_review(self):
        """Performs a code review, a task specific to Developers."""
        print(f"{self.name} is conducting a code review.")

# A class for calculating bonuses that relies on the abstract Employee class, following the Dependency Inversion Principle (DIP)
class BonusCalculator:
    def calculate_bonus(self, employee: Employee):
        """Utilizes abstraction to calculate an employee's bonus, supporting any Employee subclass."""
        return employee.get_bonus()

# A class for generating reports that also adheres to DIP by depending on the Employee abstraction
class ReportGenerator:
    def generate_report(self, employee: Employee):
        """Uses the Employee abstraction to generate a report, ensuring flexibility across different employee types."""
        report = employee.get_report()
        print(report)

if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    # Instantiate and use ReportGenerator to produce reports for both employee types
    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    # Calculate and display bonuses for both employee types using BonusCalculator
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    # Demonstrating role-specific actions
    manager.manage_team()
    developer.code_review()
