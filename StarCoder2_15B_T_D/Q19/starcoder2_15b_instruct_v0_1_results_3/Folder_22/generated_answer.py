def all_ints_not_div_by_num(lst):
    """
    Returns a list of all integers not divisible by 71 from index 40 to index 200, both exclusive.
    If no such integers exist, an empty list is returned.
    """
    result = []
    for i in range(40, 200):
        if lst[i] % 71 != 0:
            result.append(lst[i])
    return result