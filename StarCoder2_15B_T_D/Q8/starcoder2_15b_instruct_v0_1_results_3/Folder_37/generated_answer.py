def all_even_ints_exclusive(lst):
    """
    Returns the list of all even integers from index 1 to index 2, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(1, 2):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints