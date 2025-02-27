from index 14 to index 48, both exclusive.

def all_ints_not_div_by_num(int_list):
    """
    Returns the list of all integers not divisible by 16
    If no such integers exist in the specified range,
    the function returns an empty list.
    """
    return [x for x in int_list[14:48] if x % 16 != 0]