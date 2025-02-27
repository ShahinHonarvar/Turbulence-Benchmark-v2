def all_ints_not_div_by_num(int_list):
    """
    Returns a list of all integers not divisible by 8 from index 8 to index 9, both exclusive.
    If no such integers exist, returns an empty list.
    """
    return [num for i, num in enumerate(int_list) if i >= 8 and i < 9 and (num % 8 != 0)]