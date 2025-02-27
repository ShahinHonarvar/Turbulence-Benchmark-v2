def all_odd_ints_inclusive(int_list):
    """
    Returns the list of all odd integers from index 56 to index 98, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(int_list) if i >= 56 and i <= 98 and (num % 2 == 1)]