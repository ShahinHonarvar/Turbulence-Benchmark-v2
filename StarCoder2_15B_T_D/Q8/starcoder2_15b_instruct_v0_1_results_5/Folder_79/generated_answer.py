def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 3 to index 8, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i in range(3, 8):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints