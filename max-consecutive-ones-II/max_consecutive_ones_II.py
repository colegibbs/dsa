def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = z = current_max = absolute_max = 0
    size = len(nums) - 1
    zero_hit = False
    while j <= size:
        if zero_hit == False:
            if nums[j] == 0:
                zero_hit = True
                z = j
        else:
            if nums[j] == 0:
                current_max = 0
                j = z + 1
                zero_hit = False
                continue
        current_max += 1
        if absolute_max < current_max:
            absolute_max = current_max
        j += 1
    return absolute_max
