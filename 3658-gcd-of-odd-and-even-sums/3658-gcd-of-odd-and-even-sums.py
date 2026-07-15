class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        def GCD(sumOdd, sumEven):
            if sumOdd == 0:
                return sumEven
            if sumEven == 0:
                return sumOdd
            if sumOdd > sumEven:
                return GCD(sumOdd % sumEven, sumEven)
            else:
                return GCD(sumOdd, sumEven % sumOdd)

        return GCD(sumOdd, sumEven)
