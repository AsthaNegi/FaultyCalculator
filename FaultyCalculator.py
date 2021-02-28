#Faulty calculator by Astha Negi
while(1):

    print("Enter the operation you want to perform:")
    print("Enter 1 for addition:")
    print("Enter 2 for sub:")
    print("Enter 3 for mul:")
    print("Enter 4 for div:")
    a = int(input())
    if a < 1:
        print("invalid choice!\nTry again")
        exit()
    if a > 4:
        print("invalid choice!\nTry again")
        exit()

    print("Enter first number:")
    b = int(input())
    print("Enter second number:")
    c = int(input())

    if a == 1:
        if b == 33:
            if c == 11:
                print("the addition is:", 66)
            else:
                print("the addition is:", b + c)
        else:
            print("the addition is:", b + c)
    elif a == 2:
        if b == 33:
            if c == 11:
                print("the sub is:", 55)
            else:
                print("the sub is:", b - c)
        else:
            print("the sub is:", b - c)
    elif a == 3:
        if b == 33:
            if c == 11:
                print("the multiplication is:", 44)
            else:
                print("the multiplication is:", b * c)
        else:
            print("the multiplication is:", b * c)
    elif a == 4:
        if b == 33:
            if c == 11:
                print("division is:", 22)
            else:
                print("division is:", b / c)
        else:
            print("division is:", b / c)
    print("Do you want to continue?")
    print("Enter y for yes n for no")
    d = input()
    if d == "y":
        continue
    elif d=="n":
        exit()
    else:
        print("invalid choice")

