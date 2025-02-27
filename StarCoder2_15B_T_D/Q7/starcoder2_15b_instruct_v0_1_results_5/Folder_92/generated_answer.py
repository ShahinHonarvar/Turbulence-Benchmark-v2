def all_even_ints_inclusive(ints):
    """
    Returns the list of all even integers from index 0 to index 1, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in ints:
        if i % 2 == 0:
            result.append(i)
    return result