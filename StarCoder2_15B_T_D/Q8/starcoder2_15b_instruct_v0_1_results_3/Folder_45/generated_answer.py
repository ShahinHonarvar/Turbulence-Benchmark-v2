def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 30 to index 200, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_nums = []
    for i in range(30, 200):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums