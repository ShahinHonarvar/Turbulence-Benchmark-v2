def all_ints_div_by_num(ints):
    """
    Returns the list of all integers divisible by 90 from index 57 to index 67, both inclusive.
    If no such integers exist in the specified range, the function returns an empty list.
    """
    result = []
    for i in range(57, 68):
        if ints[i] % 90 == 0:
            result.append(ints[i])
    return result