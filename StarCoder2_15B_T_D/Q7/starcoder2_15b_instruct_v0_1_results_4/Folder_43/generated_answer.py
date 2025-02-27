def all_even_ints_inclusive(my_list):
    """
    Returns the list of all even integers from index 68 to index 86, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i in range(68, 87):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints