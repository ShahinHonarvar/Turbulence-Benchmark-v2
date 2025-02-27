def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 0 to index 4, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(0, 4):
        if ints[i] % 2 == 0:
            even_ints.append(ints[i])
    return even_ints