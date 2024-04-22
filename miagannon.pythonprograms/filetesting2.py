"""
file = open("names.txt","a")
file.write("James Stewart")
file.write("Hollywood")
file.close()
#write to a file using a variable
balance = 100
file = open("numbers.txt","w")
file.write(str(balance))
file.write("\n")
file.close()# close file then open in read mode to use readline correctly
file = open("numbers.txt","r")
print ("first readline",file.readline())
file.close()

balance = balance + 500
file = open("numbers.txt","a")
file.write("\n")
file.write(str(balance))
file.close()
file = open("numbers.txt","r")
print ("2nd readline",file.readline())
print ("3rd readline",file.readline())
print ("4th readline",file.readline())

file.close()
#wont work as file opened in append mode and is now positioned at end of file

"""

def readATMFile():
    global ATMbalance, pin
    bankFile = open("atm.txt", "r")
    ATMbalance = float(bankFile.readline())
    bankFile.close()
# A function to write balance to the file
def writeATMFile():
    global ATMbalance, pin
    with open('atm.txt', 'w') as bankFile:
        bankFile.write(str(ATMbalance))
        bankFile.write("\n")
#file = open("atm.txt","x")
#file.close()

readATMFile()
print("ATMBalance",ATMbalance)
ATMbalance = ATMbalance + 100.00
writeATMFile()
print("ATMBalance",ATMbalance)
        
