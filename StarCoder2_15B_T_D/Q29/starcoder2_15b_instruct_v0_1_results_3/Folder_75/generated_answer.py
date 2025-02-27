def gcf_two_nums(nums):
    """
    Returns the greatest common factor of the integers at indices 42 and 25.
    """
    a = nums[42]
    b = nums[25]
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a