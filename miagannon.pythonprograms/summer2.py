num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
choice = input("enter operation (a for addition, s for subtraction): ").lower()

if choice == 'a':
    print(num1 + num2)
elif choice == 's':
     print(num1 - num2)
else:
    print("invalid option")