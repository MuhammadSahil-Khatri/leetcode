class Solution:
    def isPalindrome(self, x: int) -> bool:
        orgNum = x
        if x < 0:
            return False
        
        revNum = 0
        while x > 0:
            dig = x % 10
            revNum = revNum * 10 + dig
            x = x // 10

        return revNum == orgNum