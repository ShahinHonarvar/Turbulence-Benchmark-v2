def sum_odd_ints_inclusive(int_list):
    """
    Returns the sum of all odd integers from index 6 to index 8, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(6, 9):
        if int_list[i] % 2 == 1:
            sum += int_list[i]
    return sum