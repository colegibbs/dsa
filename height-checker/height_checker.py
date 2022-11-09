from add-two-numbers.solution import Solution

print(Solution)

class Solution:
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        def partition(list, low, high):
            pivot = list[high]
            i = low - 1
            for j in range(low, high):
                if list[j] <= pivot:
                    i += 1
                    list[i], list[j] = list[j], list[i]
            list[i + 1], list[high] = list[high], list[i + 1]
            return i + 1

        def quickSort(list, low, high):
            if low < high:
                part_index = partition(list, low, high)
                quickSort(list, low, part_index - 1)
                quickSort(list, part_index + 1, high)

        size = len(heights)
        expected_heights = heights[:]
        quickSort(expected_heights, 0, size - 1)
        desc = 0
        for i in range(size):
            if heights[i] != expected_heights[i]:
                desc += 1
        return desc
