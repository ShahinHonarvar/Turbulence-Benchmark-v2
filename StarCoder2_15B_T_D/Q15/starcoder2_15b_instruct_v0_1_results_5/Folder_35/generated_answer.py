def sum_odd_ints_inclusive(int_list):
    """
    Returns the sum of all odd integers from index 30 to index 48, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(30, 50):
        if int_list[i] % 2 == 1:
            result += int_list[i]
    return result