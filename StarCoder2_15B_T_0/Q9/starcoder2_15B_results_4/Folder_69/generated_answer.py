def all_odd_ints_inclusive(int_list):
    """
    Returns the list of all odd integers from index 32 to index 35, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(int_list) if i >= 32 and i <= 35 and (num % 2 == 1)]