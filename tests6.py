import unittest
import laba6

class Test6(unittest.TestCase):
    def test_list(self):
        llist = laba6.LinkedList()
        llist.append(3)
        llist.append(1)
        llist.append(2)

        llist.sort_list()
        self.assertEqual(llist.__str__(),"{1 2 3 }")

if __name__ == "__main__":
    unittest.main()     
