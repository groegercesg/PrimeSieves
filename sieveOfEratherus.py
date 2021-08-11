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