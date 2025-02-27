def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 37 to index 76, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i, num in enumerate(nums):
        if i >= 37 and i <= 76 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints