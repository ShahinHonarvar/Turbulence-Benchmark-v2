def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 87 to index 95, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    evens = [i for i in ints if i % 2 == 0]
    return evens[87:95]