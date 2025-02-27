def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 7, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i, num in enumerate(nums):
        if num % 2 == 1 and 0 <= i <= 7:
            odd_ints.append(num)
    return odd_ints