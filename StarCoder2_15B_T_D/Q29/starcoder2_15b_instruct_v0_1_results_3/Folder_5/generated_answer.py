def gcf_two_nums(nums):
    """
    Returns the greatest common factor of the integers at indices 23 and 45.
    """
    return gcf(nums[23], nums[45])

def gcf(a, b):
    """
    Returns the greatest common factor of a and b.
    """
    while b != 0:
        a, b = (b, a % b)
    return a