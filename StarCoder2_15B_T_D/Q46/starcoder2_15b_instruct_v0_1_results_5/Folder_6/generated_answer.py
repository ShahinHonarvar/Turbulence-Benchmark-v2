def gcf_three_nums(nums):
    """
    Function to find the greatest common factor of the elements at indices 93, 94, and 57.

    Args:
        nums (list): A list of positive integers.

    Returns:
        int: The greatest common factor of the elements at indices 93, 94, and 57.
    """
    n1 = nums[93]
    n2 = nums[94]
    n3 = nums[57]
    gcf = 1
    for i in range(2, min(n1, n2, n3) + 1):
        if n1 % i == 0 and n2 % i == 0 and (n3 % i == 0):
            gcf = i
    return gcf