def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 22 to index 88, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(22, 89):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result