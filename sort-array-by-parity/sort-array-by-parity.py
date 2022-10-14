def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    even = 1
    odd = 0
    while even <= len(nums) - 1:
        print(even, odd)
        if nums[odd] % 2 != 0 and nums[even] % 2 == 0:
            print("hi")
            nums[odd], nums[even] = nums[even], nums[odd]
            odd += 1
        if nums[odd] % 2 == 0:
            odd += 1
        even += 1
    return nums
