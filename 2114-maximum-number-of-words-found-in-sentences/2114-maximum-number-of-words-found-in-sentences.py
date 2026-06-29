class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            maxWords = max(sentence.count(" ") + 1, maxWords)

        return maxWords
