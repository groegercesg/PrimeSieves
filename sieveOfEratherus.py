# Sieve of Eratherus - or however you spell it

# Goal:
    # Input two numbers
    # Print a list of all primes between these two bounds

# Algo:
    # Make an initial list of all numbers to test
    # Iterate through list
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

def listTest(startNum, endNum):
    initList = makeInitList(startNum, endNum)
    print(initList)
