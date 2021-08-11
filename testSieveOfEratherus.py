from sieveOfEratherus import sieve
import unittest

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
        self.assertEqual(sieve(0, 10), [2,3,5,7], "Test one through to ten")
            
  

if __name__ == "__main__":
    unittest.main()
