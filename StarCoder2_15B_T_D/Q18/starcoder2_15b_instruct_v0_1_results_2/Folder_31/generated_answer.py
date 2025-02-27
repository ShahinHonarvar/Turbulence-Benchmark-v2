def sum_ints_div_by_either_nums(ints):
    """
    Returns the sum of all integers divisible by either -59 or -79 from index 56 to index 88, both inclusive.
    If no such integers exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(56, 89):
        if ints[i] % -59 == 0 or ints[i] % -79 == 0:
            sum += ints[i]
    return sum