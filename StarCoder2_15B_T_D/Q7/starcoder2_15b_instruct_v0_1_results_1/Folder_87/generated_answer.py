def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 36 to index 46, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(36, 47):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints