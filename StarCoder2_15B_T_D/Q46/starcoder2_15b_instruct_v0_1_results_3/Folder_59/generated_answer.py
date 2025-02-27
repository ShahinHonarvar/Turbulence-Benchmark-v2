def gcf_three_nums(nums):
    """
    Returns the greatest common factor of the elements at indices 7, 6, and 8 in a list of positive integers.
    """
    num_1 = nums[7]
    num_2 = nums[6]
    num_3 = nums[8]
    gcf = num_1
    while gcf != num_2 and gcf != num_3:
        gcf -= 1
    return gcf