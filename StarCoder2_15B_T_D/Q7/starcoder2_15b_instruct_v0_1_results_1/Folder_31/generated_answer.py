def all_even_ints_inclusive(my_list):
    """
    Returns the list of all even integers from index 75 to index 88, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(75, 89):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints