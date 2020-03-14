
def add_function(a, b):

    def add_recursion(x, y):

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



add_function_test_values = {
    (+0, +7): +7,
    (+7, +0): +7,
    (+2, +2): +4,
    (+3, +2): +5,
    (+2, +3): +5,
    (-3, -2): -5,
    (-2, -3): -5,
    (-2, -2): -4,
    (-5, +2): -3,
    (-2, +5): +3,
    (+5, -2): +3,
    (2, -5): -3,
}

for arguments, check_value in add_function_test_values.items():

    result = add_function(*arguments)

    if result == check_value:
        print(f"OK! {arguments} = {result}.\n")

    else:
        print(f"WRONG! {arguments} = {result}. Must be {check_value}!\n")