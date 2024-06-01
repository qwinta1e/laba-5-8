import unittest
import laba5

class Test5(unittest.TestCase):
    def test_longestCommonPrefix(self):
        self.assertEqual(laba5.longestCommonPrefix(["python", "pythagorean", "pyramid"]), "py")
        self.assertEqual(laba5.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(laba5.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(laba5.longestCommonPrefix(["", "abc", "def"]), "")
        self.assertEqual(laba5.longestCommonPrefix([]), "")
        self.assertEqual(laba5.longestCommonPrefix(["Home", "Homie", "Homrad"]), "Hom")
    def test_findMissingNumber(self):
        self.assertEqual(laba5.findMissingNumber([1,2,3,4,5,6,8,9,10],10), 7)
        self.assertEqual(laba5.findMissingNumber([5,1,3,4,7,9,6,8,2],10), 10)
        self.assertEqual(laba5.findMissingNumber([1,2,3,5,6,7,8,9,10,11,12],12), 4)
    def test_romanToInteger(self):
        self.assertEqual(laba5.romanToInteger('XIX'),19)
        self.assertEqual(laba5.romanToInteger('MDCLXVI'),1666)
    def test_areAnagrams(self):
        self.assertTrue(laba5.areAnagrams(*['elvis', 'lives']), True)
        self.assertFalse(laba5.areAnagrams(*['elvis', 'elives']), False)
        self.assertFalse(laba5.areAnagrams(*['boba', 'biba']), False)
        self.assertTrue(laba5.areAnagrams(*['elvis', 'lives', 'viles']), True)
    def test_fibonacciNumber(self):
        self.assertEqual(laba5.fibonacciNumber(4),3)
        self.assertEqual(laba5.fibonacciNumber(10),55)
        self.assertEqual(laba5.fibonacciNumber(23),28657)

if __name__ == "__main__":
    unittest.main()        