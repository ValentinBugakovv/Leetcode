"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s, counter_t = defaultdict(int), defaultdict(int)
        for i in s:
            counter_s[i] += 1
        for i in t:
            counter_t[i] += 1
        return counter_s == counter_t

"""
Time complexity: 
O(n+m)
Space complexity: 
O(1) since we have at most 26 different characters.
"""
