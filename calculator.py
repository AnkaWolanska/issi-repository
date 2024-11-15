"""Implementing class Calculator"""

class Calculator:
    """Perform calculations"""
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        """Perform sum"""
        return self.op1 + self.op2

    def subtract(self):
        """Perform subtract"""
        return self.op1 - self.op2

    def multiply(self):
        """Perform multiplying"""
        return self.op1 * self.op2

    def divide(self):
        """Perform division"""
        return self.op1 / self.op2
