import decimal

class Precision:
    def __init__(self, precision):
        self.precision = precision
        self.current_precision = decimal.getcontext().prec


    def __enter__(self):
        decimal.getcontext().prec = self.precision


    def __exit__(self, ex_type, ex_value, ex_traceback):
        decimal.getcontext().prec = self.current_precision
        return False
