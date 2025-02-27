def sum_odd_ints_inclusive(integer_list):
    """
    Returns the sum of all odd integers from index 12 to index 92, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd = 0
    for i in range(12, 93):
        if integer_list[i] % 2 != 0:
            sum_odd += integer_list[i]
    return sum_odd