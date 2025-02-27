def all_even_ints_exclusive(ints):
    """
    Return the list of all even integers from index 86 to index 89, both exclusive.
    If no even integers exist in the specified range, return an empty list.
    """
    return [i for i in ints[86:89] if i % 2 == 0]