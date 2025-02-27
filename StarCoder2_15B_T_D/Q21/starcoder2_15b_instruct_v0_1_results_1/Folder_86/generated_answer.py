def all_ints_div_by_num(ints):
    """
    Returns the list of all integers divisible by 88 from index 44 to index 73, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(44, 74):
        if ints[i] % 88 == 0:
            result.append(ints[i])
    return result