import time
import unittest
from main import rk_algorithm

class TestRKAlgorithm(unittest.TestCase):

    def test_rk_algorithm1(self):
        patternStr = "abcdefgh"
        searchStr = "abcdefgh"
        charCount = 64
        maxPrime = 99999

        expected_output = [0]
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)
    def test_rk_algorithm2(self):
        patternStr = "abcdefgh"
        searchStr = "ijklmnop"
        charCount = 64
        maxPrime = 99999

        expected_output = []
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)
    def test_rk_algorithm3(self):
        patternStr = ""
        searchStr = "abcdefgh"
        charCount = 64
        maxPrime = 99999

        expected_output = [0,1,2,3,4,5,6,7]
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)
    def test_rk_algorithm4(self):
        patternStr = "aaa"
        searchStr = "aaaaaaaaaaaaaaaa"
        charCount = 64
        maxPrime = 99999

        expected_output = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)
    def test_rk_algorithm5(self):
        patternStr = "abcabcabcabcabcabcabc"
        searchStr = "abcabcabcabcabc"
        charCount = 64
        maxPrime = 99999

        expected_output = []
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)
    def test_rk_algorithm6(self):
        patternStr = "abc"
        searchStr = ""
        charCount = 64
        maxPrime = 99999

        expected_output = []
        result = rk_algorithm(patternStr, searchStr, charCount, maxPrime)
        self.assertEqual(result, expected_output)



if __name__ == '__main__':

  x = unittest.TestLoader().loadTestsFromTestCase(TestRKAlgorithm)
  unittest.TextTestRunner().run(x)

