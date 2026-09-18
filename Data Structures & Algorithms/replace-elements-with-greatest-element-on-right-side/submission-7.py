class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            arr[i] = max(arr[i+1:n])
        arr[n-1] = -1
        return arr
        