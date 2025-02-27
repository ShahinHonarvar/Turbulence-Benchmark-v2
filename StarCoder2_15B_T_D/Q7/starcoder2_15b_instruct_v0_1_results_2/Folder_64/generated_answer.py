def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 0 to index 4, both inclusive.
    If no even integers exist in the specified range, the function returns an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if i >= 0 and i <= 4 and (num % 2 == 0):
            result.append(num)
    return result