import unittest
import laba7

class Test7(unittest.TestCase):
    def test_count_ways(self):
        self.assertEqual(laba7.count_ways(2),2)
        self.assertEqual(laba7.count_ways(5),8)
        self.assertEqual(laba7.count_ways(10),89)
        self.assertEqual(laba7.count_ways(20),10946)
    def test_max_substring(self):
        self.assertEqual(laba7.max_substring("кокошнель"), 2)
        self.assertEqual(laba7.max_substring("аааасаааа"), 8)
        self.assertEqual(laba7.max_substring("бибобибаби"), 5)
        self.assertEqual(laba7.max_substring("кокшнель"), 2)
        self.assertEqual(laba7.max_substring("аватар"), 3)
    def test_all_paths(self):
        self.assertEqual(laba7.all_paths(5,6), 126)
        self.assertEqual(laba7.all_paths(10,10), 48620)
    def test_levenshtein_alg(self):
        self.assertEqual(laba7.levenshtein_alg("string1", "string2"), 1)
        self.assertEqual(laba7.levenshtein_alg("слон", "стол"), 2)
        self.assertEqual(laba7.levenshtein_alg("маршрут", "штурман"), 7)

if __name__ == "__main__":
    unittest.main()        