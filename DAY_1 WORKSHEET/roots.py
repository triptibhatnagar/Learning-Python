a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + D**0.5) / (2*a)
    root2 = (-b - D**0.5) / (2*a)
    print("The roots are real and distinct.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif D == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root:", root)
else:
    root1 = -b / (2*a)
    root2 = (D**0.5) / (2*a)
    print("The roots are complex.")
    print("Root 1:", root1, "+", root2, "i")
    print("Root 2:", root1, "-", root2, "i")