def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 262 to index 746, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(nums):
        if i >= 262 and i <= 746 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints