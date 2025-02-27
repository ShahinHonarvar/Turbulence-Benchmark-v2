def all_even_ints_exclusive(my_list):
    """
    Returns the list of all even integers from index 30 to index 200, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(30, 200):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints