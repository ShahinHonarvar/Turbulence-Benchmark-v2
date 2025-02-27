def gcf_three_nums(nums):
    """
    Find the greatest common factor of the elements at indices 18, 37, and 43 in a list of positive integers.
    """
    a = nums[18]
    b = nums[37]
    c = nums[43]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        b, c = (c, b % c)
    return c