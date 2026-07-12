class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ans = []
        s = s[::-1]

        i = 0
        while i < n:
            print(i)
            word = []

            while i < n and s[i] != " ":
                word.append(s[i])
                i += 1

            word = "".join(word[::-1])

            if len(word) != 0:
                ans.append(word)

            i += 1

        return " ".join(ans)
