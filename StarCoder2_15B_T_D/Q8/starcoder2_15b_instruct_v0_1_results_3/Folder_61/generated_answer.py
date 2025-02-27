def all_even_ints_exclusive(int_list):
    """
    Returns the list of all even integers from index 0 to index 7, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(0, 7):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints