# Andrew Grant 1/31/25
# Write a program that iterates from 1 to 100 and determines if each
# number is prime or not. Show all numbers from 1 to 100 and must be
# extensible to any postive integer, don't hardcode 100.


#function to check if iNum is prime
def prime(num):
    if (num < 2):
        #Anything  less than 2 isn't prime
        return False
    #Checks if the number is divisible by any integer from 2 up to num's square root
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

#iMaxNum is integer provided by user to check up to
iMaxNum = int(input("Enter upper value to check: "))
#iNum is integer to check and serves as a counter
iNum = 1

#Loop to print what is prime and what isnt
while (iNum <= iMaxNum):
    bPrime = prime(iNum)
    if (bPrime == True):
        print(iNum, "is prime")
    elif (bPrime == False):
        print(iNum, "is not prime")
    #Increments iNum every iteration of loop
    iNum += 1