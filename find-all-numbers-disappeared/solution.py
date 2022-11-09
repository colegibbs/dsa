def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lost_nums = []
    length = len(nums)
    for i in range(0, length):
        index_number = nums[abs(nums[i]) - 1]
        if index_number > 0:
            nums[abs(nums[i]) - 1] *= -1
    for j in range(0, length):
        if nums[j] > 0:
            lost_nums.append(j + 1)
    return lost_nums
