"""
Logic:
for i,j in: 1 <= i <= j
Remove if: i + j + 2ij < n
Where n is the number we are searching up to
Then, we go through the list again, 
double the remaining numbers, and add 1, to get the primes
# List:
(1,1) = 4
(1,2) = 9
(1,3) = 10
"""

# Get some functions from Eros
from sieveOfEratherus import makeInitList, findPosition

"""
n = 100
for i in range(1, n):
    j = i
    while (i + j + (2*i*j)) < n:
        print(i + j + (2*i*j))
        j += 1
"""

# Function to return the primes in the range provided
def sieve(startNum, endNum):
    # Creation of lists
    initList = makeInitList(startNum, endNum)
    primeList = []

    print(initList)
    for i in range(startNum, endNum):
        j = i
        while (i + j + (2*i*j)) < endNum:
            currentTarg = i + j + (2*i*j)
            # find position of currentTarg in initList
            currentPosition = findPosition(initList, currentTarg)
            # Delete it
            del initList[currentPosition]
            j += 1

    print(initList)
    makingPrimes = True
    while makingPrimes:
        madePrime = (2 * initList[0]) + 1
        if madePrime <= endNum:
            primeList.append(madePrime)
            del initList[0]
        else:
            makingPrimes = False
    
    print(primeList)

sieve(1, 10)