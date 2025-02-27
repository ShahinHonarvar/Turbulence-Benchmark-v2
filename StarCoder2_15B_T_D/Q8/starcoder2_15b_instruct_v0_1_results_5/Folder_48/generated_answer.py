def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 385 to index 999, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(385, 999):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints