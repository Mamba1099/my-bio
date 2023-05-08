import math
a = float(input("Enter the coefficient of a:"))
b = float(input("Enter the coefficient of b:"))
c = float(input("Enter the coefficient of c:"))





i = -1
discriminant = b**2 - 4 * a * c

if discriminant  > 0:
    root1 = float(-b + math.sqrt(discriminant))
    root2 = float(-b - math.sqrt(discriminant))
    print("The coefficient are:")
    print("root1 = ", + root1)
    print("root2 = ", + root2)


elif discriminant == 0: 
    root = -b / 2 * a
    print("root = ", + root)

else:
    real_root = -b / 2 * a * i   
    imaginary = math.sqrt(-discriminant) / 2 * a * i
    print("Root1=", + real_root )
    print("root2=", + imaginary )
