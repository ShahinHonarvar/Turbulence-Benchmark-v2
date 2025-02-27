def all_even_ints_exclusive(lst):
    """
    Returns the list of all even integers from index 4 to index 5, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(4, 5):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints