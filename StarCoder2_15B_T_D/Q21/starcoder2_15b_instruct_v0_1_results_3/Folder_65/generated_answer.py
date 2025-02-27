def all_ints_div_by_num(ints):
    """
    Finds all integers divisible by -59 from index 14 to index 56, both inclusive, in a given list of integers.
    """
    result = []
    for i in range(14, 57):
        if ints[i] % -59 == 0:
            result.append(ints[i])
    return result