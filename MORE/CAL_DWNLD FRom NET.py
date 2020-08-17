# Run this code in another IDE. This code is too advanced for Sololearn's IDE.

# Calculator.
def cal():
    print("This is a calculator.")
    print(
        "You choose a number, then a sign and then the last number. "
        "The signs can be plus, minus, times, **, division and modulos.")

    num1 = int(input("Number 1 --> "))
    sign = input("Sign --> ")
    num2 = int(input("Last number --> "))

    if sign == "+" or sign == "-" or sign == "*" or sign == "/":
        print("You want to calculate %s%s%s." % (num1, sign, num2))

    if sign == "+":
        result = int(num1) + int(num2)
        print("The result is %s." % (result))

    elif sign == "-":
        result = int(num1) - int(num2)
        print("The result is %s." % (result))

    elif sign == "*":
        result = num1 * num2
        print("The result is %s." % (result))

    elif sign == "/":
        result = num1 / num2
        print("The result is %s." % (result))

    elif sign == "**":
        result = num1 ** num2
        print("The result is %s." % (result))

    elif sign == "%":
        result = num1 % num2
        print("The result is %s." % (result))

    else:
        print("Something went wrong.")


# Square root function.
def sqr():
    from math import sqrt
    answer = input("Enter a number you want to find the square root of: ")

    def cals():
        result = sqrt(int(answer))
        print("The result is %s." % (result))

    print("We will now find the square root of you number.")

    if len(answer) > 0 and answer.isnumeric:
        cals()

    elif answer.isalpha:
        print("You can only use numbers.")

    elif len(answer) == 0:
        print("You must write something.")

    else:
        print("Something went wrong.")


# Vector length.
def length_vector():
    print("Enter the length of the x coordinate and the length of the y coodinate.")
    x, y = input("x and y coordinate: ").split()
    print("Your vector is (%s, %s)" % (x, y))

    from math import sqrt
    length = sqrt(int(x) ** 2) + sqrt(int(y) ** 2)
    print("The length of the vector is %s." % (length))


# Cos, Sin and Tan.
def deg():
    degr, nummer = input("Enter cos, sin or tan and then the number: ").split()
    degr = degr.lower()
    import math
    if degr == "cos":
        result = math.cos(math.radians(int(nummer)))
        print("The result is %s" % (result))

    elif degr == "sin":
        result = math.sin(math.radians(int(nummer)))
        print("The result is %s" % (result))

    elif degr == "tan":
        result = math.tan(math.radians(int(nummer)))
        print("The result is %s" % (result))

    else:
        print("Something went wrong.")


# if function.
def t_if():
    if choice == "calculator":
        cal()

    elif choice == "square root":
        sqr()

    elif choice == "vector length":
        length_vector()

    elif choice == "line slope":
        calc()

    elif choice == "degrees":
        deg()

    elif choice == "vector":
        vector()

    else:
        print("Something went wrong. Make sure you spelled correctly.")


# Vector
def vector():
    decide = input("Choose 'Vector projection', 'determinant' 'Vector degrees' or 'Dot product': ").lower()

    if decide == "vector projection":
        proj()

    elif decide == "dot product":
        dot()

    elif decide == "vector degrees":
        vec_deg()

    elif decide == "determinant":
        det()


# Derteminant
def det():
    a1, a2 = input("Enter a1 and a2: ").split()
    b1, b2 = input("Enter b1 and b2: ").split()
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    determinant = (a1 * b2) - (a2 * b1)
    print("The areal area of the parallellogram is %s." % (determinant))
    lop = input("Do you want to calculate the are of the triangle -->").lower()

    if lop == "yes":
        result = determinant * 0.5
        print("The are area of the triangle is %s." % (result))


# Dot product
def dot():
    a1, a2 = input("Enter a1 and a2: ").split()
    b1, b2 = input("Enter b1 and b2: ").split()
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    result = (a1 * b1) + (a2 * b2)
    print("The dot product is %s." % (result))


# Vector degrees
def vec_deg():
    from math import sqrt
    a1, a2 = input("Enter a1 and a2: ").split()
    b1, b2 = input("Enter b1 and b2: ").split()
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    dot = (a1 * b1) + (a2 * b2)
    length = (sqrt(a1) + sqrt(a2)) * (sqrt(b1) + sqrt(b2))
    degs = dot / length
    print("The result is %s." % (degs))


# Vector proj
def proj():
    def prik_produkt():
        return (a1 * b1) + (a2 * b2)

    def vec_length():
        from math import sqrt
        return (sqrt(b1 ** 2) + sqrt(b2 ** 2)) ** 2

    a1, a2 = input("Enter a1 and a2: ").split()
    b1, b2 = input("Enter b1 and b2: ").split()
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    def res():
        one = (prik_produkt() / vec_length()) * b1
        two = (prik_produkt() / vec_length()) * b2
        print("The result is (%s, %s)." % (one, two))

    res()


# Line slope
def calc():
    x, y = input("Enter x and y coordinates: ").split()
    x2, y2 = input("Enter the second x and y coordinates: ").split()
    ys = int(y2) - int(y)
    xs = int(x2) - int(x)
    result = int(ys) / int(xs)
    print("The line slope er %s." % (result))


print("Enter what type of calculations you want.")
print("You can choose 'Square root', 'Vector length', 'Calculator', 'Vector', 'Degrees' and 'Line slope'.")

choice = input("Enter here: ").lower()

if len(choice) > 0:
    t_if()

else:
    print("Something went wrong. Make sure you spelled it correct.")