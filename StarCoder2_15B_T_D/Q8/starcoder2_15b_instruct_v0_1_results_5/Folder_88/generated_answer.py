def all_even_ints_exclusive(int_list):
    """
    Returns the list of all even integers from index 2 to index 8, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    filtered_ints = []
    for i, num in enumerate(int_list):
        if i >= 2 and i < 8 and (num % 2 == 0):
            filtered_ints.append(num)
    return filtered_ints