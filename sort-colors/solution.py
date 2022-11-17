def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(0, len(nums)):
        current = i
        for j in range(current, len(nums)):
            smallest = j
            if nums[current] > nums[smallest]:
                nums[current], nums[smallest] = nums[smallest], nums[current]
