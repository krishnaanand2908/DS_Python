a = float(input("Enter first number: ")) # inputs first number
b = float(input("Enter second number: ")) # inputs second number
opr = input("Addition: 1\nSubtraction: 2\nMultiplication: 3\nDivision: 4\nEnter the number showed in front of the operation mentioned above\n-> ").strip() # inputs operator, .strip() is a method for strings which removes all the empty spaces from the start and end of the string

# Here opr has been checked to be equal to string of 1, 2, 3 and 4 because input fuction by default inputs string values

if opr == "1":
    print(a, "+", b, "=", a + b)

elif opr == "2":
    print(a, "-", b, "=", a - b)

elif opr == "3":
    print(a, "x", b, "=", a * b)

elif opr == "4":
    print(a, "/", b, "=", a / b)

else:
    print("Operator Not Found") # if somebody tries to outsmart our calculator by entering their ugly name in opr then our program will print this 