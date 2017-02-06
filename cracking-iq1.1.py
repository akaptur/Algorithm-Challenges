#!/usr/bin/env python
"""Cracking the Coding Interview - Interview Question 1.1

Justin Haaheim

Question:
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

import unittest

# clarifications to ask: capitalization matters? what character set are we
# using? simple solution: use a hash table


def is_unique_brute(input_string):

    char_count = dict()

    for char in input_string:
        if ord(char) in char_count:
            char_count[ord(char)] += 1
            if char_count[ord(char)] > 1:
                return False
        else:
            char_count[ord(char)] = 1

    # at this point, we've processed through the whole string, and there
    # hasn't been more than one of any character. return true
    return True


def is_unique(input_string):

    input_list = list(input_string)
    input_list.sort()  # sort in place. assuming this is a merge sort, so O(n log(n))

    for i in xrange(len(input_list)-1):  # minus one because we are comparing to the next character, so we don't need to iterate all the way to the last character
        if input_list[i] == input_list[i+1]:
            return False
    return True  # after sort, there were no two of the same characters in a row, so return True


class TestBruteMethod(unittest.TestCase):

    def test_string_1(self):
        self.assertTrue(is_unique_brute("abcdefghij"))

    def test_string_2(self):
        self.assertFalse(is_unique_brute("abcdefghija"))

    def test_string_3(self):
        self.assertTrue(is_unique_brute("dont lie"))

    def test_string_4(self):
        self.assertFalse(is_unique_brute("zqrtSVArBLOW"))

    def test_string_5(self):
        self.assertTrue(is_unique_brute("aAbBcCdD"))


class TestBetterMethod(unittest.TestCase):

    def test_string_1(self):
        self.assertTrue(is_unique("abcdefghij"))

    def test_string_2(self):
        self.assertFalse(is_unique("abcdefghija"))

    def test_string_3(self):
        self.assertTrue(is_unique("dont lie"))

    def test_string_4(self):
        self.assertFalse(is_unique("zqrtSVArBLOW"))

    def test_string_5(self):
        self.assertTrue(is_unique("aAbBcCdD"))


if __name__ == '__main__':
    unittest.main()
