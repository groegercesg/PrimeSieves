from sieveOfEratherus import sieve, isPrime
import unittest

class isPrimeUnitTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(isPrime(0), "Special", "Is 0 a prime number")

    def test_one(self):
        self.assertEqual(isPrime(1), "Special", "Is 1 a prime number")

    def test_prime(self):
        self.assertEqual(isPrime(5), "True", "Is 5 a prime number, yes")

    def test_not_prime(self):
        self.assertEqual(isPrime(4), "False", "Is 4 a prime number, no")

    def test_negative(self):
        self.assertEqual(isPrime(-4), "Special", "Is -4 a prime number, no, but it's less than 0 so we call it special")

class sieveUnitTests(unittest.TestCase):
    def test_both_negative(self):
        self.assertEqual(sieve(-5, -1), [], "Both numbers are negative") 

    def test_value_one_not_int(self):
        with self.assertRaises(ValueError) as cm:
            sieve("a", 2)
        self.assertEqual(cm.exception.args[0], "ERROR: For the range, you must enter integers")
    
    def test_value_two_not_int(self):
        with self.assertRaises(ValueError) as cm:
            sieve(2, "b")
        self.assertEqual(cm.exception.args[0], "ERROR: For the range, you must enter integers")
    
    def test_two_not_int(self):
        with self.assertRaises(ValueError) as cm:
            sieve(True, "b")
        self.assertEqual(cm.exception.args[0], "ERROR: For the range, you must enter integers")

    def test_range_wrong_positive(self):
        with self.assertRaises(ValueError) as cm:
            sieve(6, 2)
        self.assertEqual(cm.exception.args[0], "ERROR: the Starting Number cannot be bigger than the Ending Number")
    
    def test_range_wrong_negative(self):
        with self.assertRaises(ValueError) as cm:
            sieve(-2, -6)
        self.assertEqual(cm.exception.args[0], "ERROR: the Starting Number cannot be bigger than the Ending Number")
    
    def test_both_same_negative(self):
        self.assertEqual(sieve(-5, -5), [], "Both the same and negative")   

    def test_both_same_positive_prime(self):
        self.assertEqual(sieve(5, 5), [5], "Both the same, positive and prime")    
            
    def test_both_same_positive_not_prime(self):
        self.assertEqual(sieve(4, 4), [], "Both the same, positive and not prime")  

    def test_both_same_zero(self):
        self.assertEqual(sieve(0, 0), [], "Both the same, positive and zero")             

    def test_negative_and_zero(self):
        self.assertEqual(sieve(-5, 0), [], "One negative and one zero")      

    def test_zero_and_one(self):
        self.assertEqual(sieve(0,1), [], "inputs of zero and one")

    def test_one_to_ten(self):
        self.assertEqual(sieve(1, 10), [2,3,5,7], "Test one through to ten")
    
    def test_minus_five_to_five(self):
        self.assertEqual(sieve(-5, 5), [2,3,5], "Test -5 to 5")
            
  
if __name__ == "__main__":
    unittest.main()
