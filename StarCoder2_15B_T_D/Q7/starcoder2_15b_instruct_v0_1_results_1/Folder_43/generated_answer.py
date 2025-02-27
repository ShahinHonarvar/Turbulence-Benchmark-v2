def all_even_ints_inclusive(lst):
    """
    Takes a list of integers and returns the list of all even integers from index 68 to index 86, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 68 and i <= 86 and (x % 2 == 0)]