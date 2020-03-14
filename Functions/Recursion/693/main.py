from myfunction import add_function


MAX_VALUE = 10**3


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
    (2, MAX_VALUE): (MAX_VALUE + 2),
}

for arguments, check_value in add_function_test_values.items():

    result = add_function(*arguments)

    if result == check_value:
        print(f"OK! {arguments} = {result}.\n")

    else:
        print(f"WRONG! {arguments} = {result}. Must be {check_value}!\n")
