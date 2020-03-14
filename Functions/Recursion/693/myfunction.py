def recursion(a, b):
    
    # (+, +)
    if a > 0 and b > 0:

        # (3, 2) = 5
        if abs(a) > abs(b): 
            if  b == 1:
                return a+1
            else:
                return recursion(a+1, b-1)

        # (2, 3) = 5
        if abs(a) <= abs(b):            
            a, b = b, a
            print("Swapp")
            return recursion(a, b)


    # (-, -)
    if a < 0 and b < 0:

        # (-3, -2) = -5
        if abs(a) >= abs(b): 
            if  b == -1:
                return a-1
            else:
                return recursion(a-1, b+1)

        # (-2, -3) = -5
        if abs(a) < abs(b):
            a, b = b, a
            print("Swapp")
            return recursion(a, b)
  
    # (-, +)
    if a < 0 and b > 0:

        # (-5, 2) = -3
        if abs(a) > abs(b):
            if  b == 1:
                return a+1
            else:
                return recursion(a+1, b-1)
                
        
        # (-2, 5) = 3
        if abs(a) < abs(b):
            if  a == -1:
                return b-1
            else:
                return recursion(a+1, b-1)

    # (+, -)
    if a > 0 and b < 0:

        # (5, -2) = 3
        if abs(a) > abs(b):
            a, b = b, a
            print("Swapp")
            return recursion(a, b)

        # (2, -5) = -3
        if abs(a) < abs(b):
            a, b = b, a
            print("Swapp")
            return recursion(a, b)

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

