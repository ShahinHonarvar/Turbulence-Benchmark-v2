def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 1 to index 7, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(1, 7):
        if ints[i] % 2 == 0:
            even_ints.append(ints[i])
    return even_ints