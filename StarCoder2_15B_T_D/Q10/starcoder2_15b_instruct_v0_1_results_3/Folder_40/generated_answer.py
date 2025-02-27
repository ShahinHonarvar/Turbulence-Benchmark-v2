def all_odd_ints_exclusive(numbers):
    """
    Returns the list of all odd integers from index 0 to index 2, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i in range(0, 2):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints