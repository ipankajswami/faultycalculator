print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter ur choice(1/2/3/4:):"))  # choice selection
# Addition
if choice == 1:
    n1 = eval(input("Enter 1st no:"))  # input first number
    n2 = eval(input("Enter 2st no:"))  # input second number
    if n1 == 56 and n2 == 9:
        print("77")
    else:
        print(n1 + n2)

# Subtraction
elif choice == 2:
    n1 = eval(input("Enter 1st no:"))  # input first number
    n2 = eval(input("Enter 2st no:"))  # input second number
    print(n1 - n2)

# Multiplication
elif choice == 3:
    n1 = eval(input("Enter 1st no:"))  # input first number
    n2 = eval(input("Enter 2st no:"))  # input second number
    if n1 == 45 and n2 == 3:
        print("555")
    else:
        print(n1 * n2)

# Division
elif choice == 4:
    n1 = eval(input("Enter 1st no:"))  # input first number
    n2 = eval(input("Enter 2st no:"))  # input second number
    if n1 == 56 and n2 == 6:
        print("4")
    else:
        print(n1 / n2)
else:
    print("Invalid input")
