def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 0 to index 6, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(0, 7):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints