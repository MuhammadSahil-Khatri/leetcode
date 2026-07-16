from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        n = len(nums)
        prefixGcd = []
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd.append(gcd(nums[i], mx))

        prefixGcd.sort()
        i = 0
        j = n - 1
        total = 0
        while i < j:
            total += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return total
