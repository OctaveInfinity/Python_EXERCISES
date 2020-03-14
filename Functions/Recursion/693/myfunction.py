
def recursion(a, b):
    
    def template(a, b, e, s):
        # print(a, b)
        if abs(a) >= abs(b):
            if  b == 1*s:
                # print()
                return a+1*s
            else:
                return template(a+1*s*e, b-1*s*e, e, s)
        else:
            a, b = b, a
            # print("Swapp")
            return template(a, b, e, s)

    # (+, +)
    if a > 0 and b > 0:

        return template(a, b, 1, 1) # ok

    # (-, -)
    if a < 0 and b < 0:

        return template(a, b, +1, -1) # ok

    # (-, +)
    if a < 0 and b > 0:

        if abs(a) > abs(b):
            return template(a, b, 1, 1) # ok

        if abs(a) < abs(b):
            return template(a, b, -1, 1) # ok

    # (+, -)
    if a > 0 and b < 0:

        if abs(a) > abs(b):
            return template(a, b, +1, -1) # ok

        if abs(a) < abs(b):
            return template(a, b, -1, -1) # ok


    # (0, 7) = 7
    if a == 0:
        return b

    # (7, 0) = 7
    if b == 0:
        return a



# x = int(input("x: "))
# y = int(input("y: "))        

# res = recursion(x, y)
# print(res)


test_values = {
    (+0, +3): +3,
    (+3, +0): +3,
    (+3, +2): +5,
    (+2, +3): +5,
    (+2, +2): +4,
    (-3, -2): -5,
    (-2, -3): -5,
    (-2, -2): -4,
    (-5, +2): -3,
    (-2, +5): +3,
    (+5, -2): +3,
    (+2, -5): -3,
}

for key, value in test_values.items():

    if recursion(*key) == value:
        print(f'YES resursion{key} == {recursion(*key)}.')

    else:
        print(f'! Not ! resursion{key} == {recursion(*key)}. Must be {value}')