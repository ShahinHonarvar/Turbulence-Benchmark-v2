def all_odd_ints_exclusive(int_list):
    """
    Returns a list of all the odd integers in the range 389 to 748, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for num in int_list[389:748] if num % 2 == 1]