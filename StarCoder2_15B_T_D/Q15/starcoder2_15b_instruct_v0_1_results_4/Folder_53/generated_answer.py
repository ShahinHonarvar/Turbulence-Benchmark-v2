def sum_odd_ints_inclusive(int_list):
    """
    Returns the sum of all odd integers from index 300 to index 300, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd = 0
    for i in range(300, 301):
        if int_list[i] % 2 != 0:
            sum_odd += int_list[i]
    return sum_odd