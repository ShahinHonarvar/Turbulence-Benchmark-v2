def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 22 to index 50, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(22, 51):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints