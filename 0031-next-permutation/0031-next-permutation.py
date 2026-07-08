class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        n = len(arr)

        # Find the pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # If no pivot exists, reverse the entire array
        if pivot == -1:
            i = 0
            j = n - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return

        # Find the next greater element
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Reverse the suffix
        i = pivot + 1
        j = n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1