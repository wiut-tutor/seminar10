import numpy as np

class Solution:

    def binarySearchRecursive(self, sequence, x, left, right):
        if left > right:
            return False
        mid = int(np.ceil((left + right) / 2))
        print(mid)

        if (sequence[mid] == x):
            return mid
        elif x < sequence[mid]:
            return self.binarySearchRecursive(sequence, x, left, mid - 1)
        elif x > sequence[mid]:
            return self.binarySearchRecursive(sequence, x, mid + 1, right)


if __name__ == "__main__":
    solution = Solution()
    sample = [12, 13, 15, 16, 18, 20]
    print(len(sample))
    x = 16
    print('Index of number ', x, 'is equal to ', solution.binarySearchRecursive(sample, x, 0, len(sample) - 1))
