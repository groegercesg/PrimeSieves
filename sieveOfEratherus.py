# Sieve of Eratherus - or however you spell it

# Goal:
    # Input two numbers
    # Print a list of all primes between these two bounds

# Algo:
    # Make an initial list of all numbers to test
    # Iterate through list - while not empty
    # If number prime, remove from init_list, add to prime_list
        # Iterate through init_list, also remove all multiples of number
    # If number not prime 
        # Iterate through init_list, also remove all multiples of number

def isPrime(num):
    # Iterate through everything below
    # return false and break if divides no remainder (MOD)
    if num <= 1:
        return False
    if num > 2:
        for belowNum in range(2, num):
            if ((num % belowNum) == 0):
                return False
                break
        return True
    else:
        return True

# Function to make the initial List
def makeInitList(startNum, endNum):
    initList = []
    for i in range(startNum, endNum+1):
        initList.append(i)
    return initList

# Function to find position of a num in a given inList
# Returns position if found, or -1 if not
def findPosition(inList, num):
    returnValue = -1
    for i in range(0, len(inList)):
        if num == inList[i]:
            returnValue = i
            break
    return returnValue

# Function to hunt down and clean out the multiples
def multiplesClean(inList, num):
    # We assume inList is in order, with max at inList(len(inList)-1)
    print(inList)
    currentMult = num
    # We continue iterating if not over the end
    while currentMult <= inList[len(inList) - 1]:
        # find position of currentMult in inList
        currentPosition = findPosition(inList, currentMult)
        if currentPosition != -1:
            # Delete the current multiple at the set position
            del inList[currentPosition]
            # Increment the value
            currentMult += num
        else:
            # We couldn't find the current multiple in out list,
            # As we got -1 (the not found value) back from the search
            raise ValueError

    # our current multiple is now too big, so let's stop
    return inList


def sieve(startNum, endNum):
    # Creation of lists
    initList = makeInitList(startNum, endNum)
    primeList = []

    # Iteration method to loop through list Elements
    while initList != []:
        # If initList[0] is Prime, Add to primeList
        # multiples Clean
        # remove from initList (handled by: multiplesClean)
        if (isPrime()):
            print("Found a prime: " + initList[0])
            primeList.append(initList[0])
            initList = multiplesClean(initList, initList[0])


        del initList[0]
