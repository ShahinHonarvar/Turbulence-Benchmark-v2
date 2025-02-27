def all_even_ints_exclusive(int_list):
    """
    Returns the list of all even integers from index 86 to index 89, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i, num in enumerate(int_list):
        if i >= 86 and i < 89 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints