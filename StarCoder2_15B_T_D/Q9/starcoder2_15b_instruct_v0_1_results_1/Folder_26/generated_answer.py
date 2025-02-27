def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 62 to index 99, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(nums):
        if i >= 62 and i <= 99 and (num % 2 == 1):
            result.append(num)
    return result