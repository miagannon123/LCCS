
# Ask the user for the principal
principal = input("Enter principal: ")
#principal = float(principal)
principal = float(input("principal"))
# Ask the user for the interest rate
#6rate = input("Enter rate: ")
#rate = float(rate)
rate = float(input("rate"))
# Ask the user for the length of time
#time = input("Enter time in years: ")
#time = float(time)
time = float(input("time in years"))
# Simple interest calculation
amount = principal * rate * time

# Display the answer
print("The interest amount is", amount)