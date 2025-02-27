def sum_odd_ints_inclusive(int_list):
    """
    Returns the sum of all odd integers from index 29 to index 51, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd_ints = 0
    for i in range(29, 52):
        if int_list[i] % 2 == 1:
            sum_odd_ints += int_list[i]
    return sum_odd_ints