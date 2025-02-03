class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        if isinstance(numerator, str):
            fraction_str = numerator.strip()
            if "/" in fraction_str:
                fraction_parts = fraction_str.split('/')
                if len(fraction_parts) == 2:
                    strNum = int(fraction_parts[0])
                    strDenom = int(fraction_parts[1])

                    if strDenom == 0:
                        raise ZeroDivisionError("Denominator cannot be zero.")
                        
                    self.numerator = strNum
                    self.denominator = strDenom
            else:
                self.numerator = 0
                self.denominator = 1
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = 0
            self.denominator = 1

        gcd_value = Fraction.gcd(self.numerator, self.denominator)
        if gcd_value != 0:
            self.numerator //= gcd_value
            self.denominator //= gcd_value

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        while b:
            a, b = b, a % b
        return abs(a)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"