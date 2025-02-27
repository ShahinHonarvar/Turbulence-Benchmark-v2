def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 75 to index 85, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(75, 86):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result