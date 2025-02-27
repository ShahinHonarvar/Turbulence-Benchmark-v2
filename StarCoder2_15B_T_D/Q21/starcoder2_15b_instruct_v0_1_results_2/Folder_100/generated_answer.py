def all_ints_div_by_num(lst):
    """
    Returns a list of all integers divisible by 86 from index 86 to index 92, both inclusive.
    If no such integers exist, returns an empty list.
    """
    result = []
    for i in range(86, 93):
        if lst[i] % 86 == 0:
            result.append(lst[i])
    return result