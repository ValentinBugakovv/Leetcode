import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^\w\s]', '', s).lower().replace(' ', '')
      #  print(s)
        left = 0
        right = len(s) - 1
        while left < right:
       #     print(s[left], s[right])
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True 
