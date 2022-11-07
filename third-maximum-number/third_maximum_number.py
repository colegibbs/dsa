def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first_max = second_max = third_max = (-(2**31)) - 1
    for number in nums:
        print("first, second, third", [first_max, second_max, third_max])
        if number in [first_max, second_max, third_max]:
            continue
        if number > first_max:
            third_max = second_max
            second_max = first_max
            first_max = number
        elif number > second_max:
            third_max = second_max
            second_max = number
        elif number > third_max:
            third_max = number
        print("first, second, third", [first_max, second_max, third_max])
    if third_max != (-(2**31)) - 1:
        return third_max
    else:
        return first_max
