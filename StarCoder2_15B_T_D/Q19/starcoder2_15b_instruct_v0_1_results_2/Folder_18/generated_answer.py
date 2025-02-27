def all_ints_not_div_by_num(ints):
    """
    Returns the list of all integers not divisible by 41 from index 35 to index 98, both exclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    filtered = [i for i in ints if i % 41 != 0]
    return filtered[35:98] if filtered else []