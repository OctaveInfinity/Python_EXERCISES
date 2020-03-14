from mydecorator import decorator_stopwatch

# @decorator_stopwatch
def add_function(a, b):
    """The function calculates the sum of two integers.
    It uses a nested recursive function. Last one uses
    only following arithmetic operations: adding 1 or subtracting 1.
    """
    def add_recursion(x, y):
        """Nested recursive function.
        To optimize the recursion depth,
        the second operand must be absolutely
        smaller than or equal the first one.
        """
        # chek only second operand
        if y > 0:
            return add_recursion(x, y-1) + 1
        elif y < 0:
            return add_recursion(x, y+1) - 1
        else:
            # end condition: y == 0
            return x

    # optimization part
    if abs(a) >= abs(b):
        return add_recursion(a, b)
    else:
        a, b = b, a
        return add_recursion(a, b)
