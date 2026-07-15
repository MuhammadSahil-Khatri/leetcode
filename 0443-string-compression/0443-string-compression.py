class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        idx = 0
        i = 0
        while i < n:
            char = chars[i]
            charCount = 0

            while i < n and chars[i] == char:
                charCount += 1
                i += 1

            chars[idx] = char
            idx += 1
            if charCount > 1:
                for dig in str(charCount):
                    chars[idx] = dig
                    idx += 1

        return idx
