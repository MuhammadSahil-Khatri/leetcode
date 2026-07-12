class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for ch in s:
            stack.append(ch)

            if len(stack) >= m and "".join(stack[-m:]) == part:
                del stack[-m:]

        return "".join(stack)



# My First solution that works but not efficient
# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         while part in s:
#             s = s.replace(part, "", 1)
#         return s
