def all_even_ints_exclusive(lst):
    """
    This function takes a list of integers as an argument and returns the list of all even integers from index 70 to index 98, both exclusive.
    """
    return [n for i, n in enumerate(lst) if 70 < i < 98 and n % 2 == 0]