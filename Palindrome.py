# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Reverse string using slice method and compare it.
        incomingVal = str(x)[::-1]
        return incomingVal == str(x)
