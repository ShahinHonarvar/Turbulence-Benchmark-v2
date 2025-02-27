def all_ints_not_div_by_num(int_list):
    """
    Returns the list of all integers not divisible by -9 from index 7 to index 9, both exclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [i for i in int_list[7:9] if i % -9 != 0]