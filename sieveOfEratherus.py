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
    if (num <= 1):
        return "Special"
    elif (num >= 2):
        for belowNum in range(2, num):
            if ((num % belowNum) == 0):
                return "False"
                break
        return "True"
    else:
        raise ValueError

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
    currentMult = num
    # We continue iterating if not over the end
    while (inList != [] and currentMult <= inList[len(inList) - 1]):
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
            # It might have been removed by a previous multiples check
            # like 6 is a multiple of 2 and 3
            # So we just increment and continue
            currentMult += num

    # our current multiple is now too big, so let's stop
    return inList

# Function to return the primes in the range provided
def sieve(startNum, endNum):
    # Validation
    if (not isinstance(startNum, int) or not isinstance(endNum, int)):
        raise ValueError("ERROR: For the range, you must enter integers")
    elif (endNum < startNum):
        raise ValueError("ERROR: the Starting Number cannot be bigger than the Ending Number")
    elif (startNum < 0 and endNum < 0):
        # There are no primes below 0
        return []
    elif (startNum < 0):
        # Given our second validation step, if we reach here:
        # startNum being negative
        # then endNum must at least be 0, if not more
        # let's make startNum = 0, the first postive number and go from there
        startNum = 0

    # Creation of lists
    initList = makeInitList(startNum, endNum)
    primeList = []

    # Iteration method to loop through list Elements
    while initList != []:
        primeCheck = isPrime(initList[0])
        # If initList[0] is Prime, Add to primeList
        # multiples Clean
        # remove from initList (handled by: multiplesClean)
        if (primeCheck == "True"):
            #print("Found a prime: " + str(initList[0]))
            primeList.append(initList[0])
            initList = multiplesClean(initList, initList[0])
        # If not a prime, clear it and the multiples out
        elif (primeCheck == "False"):
            initList = multiplesClean(initList, initList[0])
        # If a special, like 0 or 1
        elif (primeCheck == "Special"):
            del initList[0]
        else:
            raise ValueError

    return primeList