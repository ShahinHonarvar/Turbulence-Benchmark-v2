def all_even_ints_exclusive(list):
    """
    Returns the list of all even integers from index 323 to 972, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i in range(323, 972):
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints