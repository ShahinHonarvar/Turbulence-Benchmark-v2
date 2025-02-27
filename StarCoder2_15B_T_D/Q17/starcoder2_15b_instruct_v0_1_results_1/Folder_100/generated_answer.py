def all_ints_div_by_both_two_nums(ints):
    """
    Returns the list of all integers divisible by both 32 and 44 from index 72 to index 93, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    res = []
    for i, num in enumerate(ints):
        if i >= 72 and i <= 93 and (num % 32 == 0) and (num % 44 == 0):
            res.append(num)
    return res