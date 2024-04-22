num1 = input(("Enter a number "))
num2 = input(("Enter another number "))

while True:
        print("Inside While Loop")
        choice= input("Do you want the loop to continue Y/N ")
        if choice in ("Y", "y"):
            print("continuing....")
            num1 = input(("Enter a number "))
            num2 = input(("Enter another number "))
        else:
            break
        