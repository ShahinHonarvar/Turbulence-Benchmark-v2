def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 8, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for num in nums:
        if num % 2 == 1:
            odd_ints.append(num)
    return odd_ints[:8]