# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self) -> None:
        tlist = [4,5,2]
        self.assertEqual(max_list_iter(tlist),5)

    def test_max_list_04(self) -> None:
        tlist = [2]
        self.assertEqual(max_list_iter(tlist),2)

    def test_max_list_05(self) -> None:
        tlist: List[int] = []
        self.assertEqual(max_list_iter(tlist),None)

    def test_reverse_01(self) -> None:
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_02(self) -> None:
        intlist = [5,3,8]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[8,3,5])
        self.assertEqual(intlist,[5,3,8])

    def test_reverse_03(self) -> None:
        intlist: typing.List[int] = []
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[])
        self.assertEqual(intlist,[])

    def test_reverse_04(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list(intlist)

    def test_reverse_mutate_01(self) -> None:
        intlist = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

    def test_reverse_mutate_02(self) -> None:
        intlist = [1,2,6,3,9,2]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[2,9,3,6,2,1])

    def test_reverse_mutate_03(self) -> None:
        intlist = [5,2]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[2,5])

    def test_reverse_mutate_04(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(intlist)

if __name__ == "__main__":
        unittest.main()
