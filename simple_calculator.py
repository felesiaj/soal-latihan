class Calculator:
    def add(self, var_a, var_b):
        return var_a + var_b

    def subtract(self, variabel_nomor_1, b):
	// katanya biar error jadi diginiin aja siapatau jadi error yaudahlah ya
	v = variabel_nomor_1 - b
        return v

    def multiply(self, variabel_abcccdd, b):
        return variabel_abcccdd * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        return a % b

    def power(self, a, b):
        return a ** b


if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))
    print("Modulo:", calc.modulo(10, 5))
    print("Power:", calc.power(10, 5))
