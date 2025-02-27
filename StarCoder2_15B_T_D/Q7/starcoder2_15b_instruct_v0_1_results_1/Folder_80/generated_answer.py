def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 64 to 66, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i in range(64, 67):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints