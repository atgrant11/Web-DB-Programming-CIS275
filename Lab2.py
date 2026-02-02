# Andrew Grant 2/2/26

#Create a python program that will accept a password from a user.
#If the given password is not at least 8 characters in length, ask for 
#a new password. Continue until a long enough password is given. 
#Do not use a loop with a break or a continue statement.
#Create a function called buildABetterPassword that takes the password 
#(that has been validated as far as length goes), and returns a new password. 
# Do not use any global variables.

#Function to change characters in password
def buildABetterPassword (sInput):
    #List that starts empty and has the for loop add characters
    lBetterPass = ""

    #examines each character from the user input and makes changes as needed
    for char in sInput:
        if (char == "e") or (char == "E"):
            lBetterPass += "3"
        elif (char == "i") or (char == "I"):
            lBetterPass += "7"
        elif (char == "l") or (char == "L"):
            lBetterPass += "1"
        elif (char == "o") or (char == "O"):
            lBetterPass += "0"
        elif (char == "p") or (char == "P"):
            lBetterPass += "9"
        elif (char == "s") or (char == "S"):
            lBetterPass += "$"
        elif (char == "1"):
            lBetterPass += "!"
        elif (char == " "):
            lBetterPass += "_"
        else:
            lBetterPass += char

    #Finds the middle character, replaces with an @
    middle = len(lBetterPass) // 2
    lBetterPass = lBetterPass[:middle] + "@" + lBetterPass[middle+1:]

    return lBetterPass

#Asks user to enter a password
sInput = str(input("Enter a password: "))

#Checks length of user input and asks for new input until it is long enough.
while (len(sInput) < 8):
    print("\nSorry that password isn't long enough.")
    sInput = str(input("Enter a new password: "))

#Saves returned new password
sNewPass = buildABetterPassword(sInput)
print(f"A better password would be {sNewPass}, it is {len(sNewPass)} characters long.")
