import data
import lab6
import unittest
from data import Book
from lab6 import selection_sort_books, swap_case, str_translate, histogram


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_book1(self):
        books = [Book(2,"The Great Gatsby"), Book(1,"1984"), Book(3,"To Kill a Mockingbird")]
        selection_sort_books(books)
        self.assertEqual([book.title for book in books],["1984", "The Great Gatsby", "To Kill a Mockingbird"])


    # Test case with an empty list
    def test_selection_sort_book2(self):
        empty_books = []
        selection_sort_books(empty_books)
        self.assertEqual(empty_books,[])

    # Part 2
    def test_swapcase1(self):
        word1 = "Millie Lombera"
        actual = swap_case(word1)
        self.assertEqual("mILLIE lOMBERA",actual)
    def test_swapcase2(self):
        word1 = "mILLIE lOMBERA"
        actual = swap_case(word1)
        self.assertEqual("Millie Lombera", actual)

    # Part 3
    def test_str_transalte1(self):
        test1 = str_translate('abcdcba', 'a', 'x')
        actual = "xbcdcbx"
        self.assertEqual(test1, actual)

    def test_str_transalte2(self):
        test2 = str_translate('hello world', 'o', '0')
        actual = "hell0 w0rld"
        self.assertEqual(test2,actual)
    # Part 4
    def test_histogram(self):
        test1 = histogram("WOW Hello")
        actual = {'W': 2, 'O': 1, ' ': 1, 'H': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(test1,actual)

    def test_histogram2(self):
        test = histogram("Millie Lombera")
        actual = {'M': 1, 'i': 2, 'l': 2, 'e': 2, ' ': 1, 'L': 1, 'o': 1, 'm': 1, 'b': 1, 'r': 1, 'a': 1}
        self.assertEqual(test,actual)



if __name__ == '__main__':
    unittest.main()
