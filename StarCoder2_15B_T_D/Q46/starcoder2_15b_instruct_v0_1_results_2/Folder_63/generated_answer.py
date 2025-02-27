def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    """
    Finds the greatest common factor of the elements at indices 38, 52, and 69 of a list.

    Args:
        nums (list): A list of positive integers.

    Returns:
        int: The greatest common factor of the elements at indices 38, 52, and 69.
    """
    gcf_38_52 = gcf(nums[38], nums[52])
    return gcf(gcf_38_52, nums[69])