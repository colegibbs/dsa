def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = 0
        right = length - 1
        result = list(range(0, length))
        
        for i in range(len(result) - 1, -1, -1):
            print(i)
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        
        return result