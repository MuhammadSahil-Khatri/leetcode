class Solution:
    def reverse(self, x: int) -> int:
        maxLimit = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0
        while x > 0:
            dig = x % 10
            ans = ans * 10 + dig

            x = x // 10

        if ans > maxLimit:
            return 0 

        if sign == -1:
            return  sign * ans
        else:
            return ans