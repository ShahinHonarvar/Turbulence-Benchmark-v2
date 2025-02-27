def all_odd_ints_inclusive(nums):
    """
    Returns all odd integers from index 8 to index 9, both inclusive.
    If no odd integers exist in the specified range, the function returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(nums):
        if i >= 8 and i <= 9 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints