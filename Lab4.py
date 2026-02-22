# Andrew Grant 2/22/26
# Create a program that will help you familiarize yourself with various data structures
# available in the Python language.
# You are the owner of a very successful hamburger restaurant. Your faithful customers line up 
# every day and eat dozens of burgers. You are writing a program to track exactly how many 
# hamburgers each customer eats.

import random

def randomName() :
    #Fill this list with at least 8 names.
    asCustomers = ["Lando", "Oscar", "Max", "Isack", "Sergio", "Valtteri", "George", "Kimi"]
    iRandomNum = random.randint(0,len(asCustomers)-1)
    return asCustomers[iRandomNum]

def randomBurgers() :
    return random.randint(1, 20)

# Queue
qCustomers = []

# Dictionary
dictCustomers = {}

for i in range(100):
    qCustomers.append(randomName())

while len(qCustomers) > 0:
    sCustomerName = qCustomers.pop(0)
    #Add customer to dictionary if not present
    if sCustomerName not in dictCustomers:
        dictCustomers[sCustomerName] = 0
    #Increment burger total
    dictCustomers[sCustomerName] += randomBurgers()

#Sorted list of tuples (descending)
listSortedCustomers = []

for name, burgers in dictCustomers.items():
    listSortedCustomers.append((name, burgers))

#sort by burger count descending
listSortedCustomers.sort(key=lambda x: x[1], reverse=True)


for name, burgers in listSortedCustomers:
    print(f"{name:20s} {burgers:3d}")