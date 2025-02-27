def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 13 to index 76, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i, num in enumerate(ints):
        if i >= 13 and i < 76 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints