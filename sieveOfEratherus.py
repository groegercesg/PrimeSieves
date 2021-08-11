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

def makeInitList(startNum, endNum):
    initList = []
    for i in range(startNum, endNum+1):
        initList.append(i)
    return initList

def multiplesHunt(list, num):


def sieve(startNum, endNum):
    # Creation of lists
    initList = makeInitList(startNum, endNum)
    primeList = []

    # Iteration method to loop through list Elements
    while initList != []:
        # If initList[0] is Prime, Add to primeList
        # multiples Hunt
        # remove from initList
        if (isPrime()):
            print("Found a prime: " + initList[0])
            primeList.append(initList[0])
            initList = multiplesHunt(initList, initList[0])


        del initList[0]
