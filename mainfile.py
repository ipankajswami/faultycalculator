oplist = ["+", "-", "*", "/"]

num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))


op = input("Enter Your operation")

if op in oplist[0]:
    if num1 == 56 and num2 ==9:
        print("sum is : 77")
    else:
        print("sum is :", num1+num2)

elif op in oplist[1]:
    if num1 == 89 and num2 == 56:
        print("subtraction is : 865")
    else:
        print("subtraction is :",num1-num2) 

elif op in oplist[2]:
    if num1 == 45 and num2 == 3:
        print("multiplication is : 555")
    else:
        print("multiplication is :", num1*num2)


elif op in oplist[3]:
    if num1 == 56 and num2 == 6:
        print("division is : 4")
    else:
        print("division is :", num1/num2)

else:
    print("you have Choose invalid operation ! ")
