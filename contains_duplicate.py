"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

# Решение черещ HashSet
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False # Time O(n), Space O(n)



# HashSet len
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) # Time O(n), Space O(n)


# Defualtdict
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        if sorted(d.items(), key=lambda x: x[1], reverse=True)[0][1] == 1:
            return False
        else:
            return True # Time O(nlogn), Space O(n)




      
