def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 0 to index 10, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i in range(len(lst)):
        if i >= 0 and i <= 10:
            if lst[i] % 2 == 0:
                even_ints.append(lst[i])
    return even_ints