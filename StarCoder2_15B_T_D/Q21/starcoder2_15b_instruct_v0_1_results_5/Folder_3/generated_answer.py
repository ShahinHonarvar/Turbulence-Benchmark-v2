def all_ints_div_by_num(lst):
    """
    Returns the list of all integers divisible by -26 from index 25 to index 59, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 59 and (x % -26 == 0)]