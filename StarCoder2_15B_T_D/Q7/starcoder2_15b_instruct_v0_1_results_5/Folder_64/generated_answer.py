def all_even_ints_inclusive(int_list):
    """
    Return the list of all even integers from index 0 to index 4, both inclusive.
    If no even integers exist in the specified range, return an empty list.
    """
    even_ints = []
    for i in range(5):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints