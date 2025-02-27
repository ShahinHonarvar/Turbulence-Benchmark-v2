def all_ints_div_by_num(int_list):
    """
    Returns a list of all integers divisible by -63 from index 31 to index 72, both inclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(int_list) if i >= 31 and i <= 72 and (num % -63 == 0)]