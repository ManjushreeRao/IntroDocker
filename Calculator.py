def addition(a,b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = a / b
    return c

class Calculator:
    result = 0

def init (self):
    pass

def add(self, a, b):
    self.result = addition(a, b)
    return self.result

def subtract(self, a, b):
    self.result = subtraction(a, b)
    return self.result

def mul(self, a, b):
    self.result = multiplication(a, b)
    return self.result

def div(self, a, b):
    self.result = division(a, b)
    return self.result