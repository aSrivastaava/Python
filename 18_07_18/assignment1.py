# Write a menu driven program to compute GCD of two numbers, find the power of number and find a factorial of the number.

def GCD(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    print("GCD = ", gcd)
    return

def power(x, y):
    poxy = 1
    for pox in range(1, y + 1):
        poxy = poxy * x

    print(poxy)
    return

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i

    print("The factorial of ", x, " is : ", fact)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

choice = int(input("Press 1 for GCD \nPress 2 for Power \nPress 3 for Factorial\n"))

if(choice==1):
    GCD(number1, number2)
elif(choice==2):
    power(number1, number2)
elif(choice==3):
    number = int(input("Enter the number to have its Factorial"))
    factorial(number)
