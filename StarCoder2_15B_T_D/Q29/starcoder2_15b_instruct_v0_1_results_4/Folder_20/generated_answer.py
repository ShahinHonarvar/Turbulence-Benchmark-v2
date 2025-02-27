def gcf_two_nums(nums):
    """
    Returns the greatest common factor of the integers at indices 19 and 94 in the given list of positive integers.
    """
    num1 = nums[19]
    num2 = nums[94]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1