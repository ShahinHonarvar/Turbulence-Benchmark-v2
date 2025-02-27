def all_even_ints_exclusive(integers):
    """
    Given a list of integers, return the list of all even integers from index 64 to index 80, both exclusive.
    If no even integers exist in the specified range, return an empty list.
    """
    return [integer for i, integer in enumerate(integers) if i >= 64 and i < 80 and (integer % 2 == 0)]