from the given list. If no positive integers exist in the specified range,

def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers in the range 75 to 88 (inclusive)
    the function returns an empty list.
    """
    return [x for x in lst[75:90] if x > 0]