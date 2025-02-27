def sum_odd_ints_inclusive(ints_list):
    """
    Function to sum all odd integers from index 246 to index 750, both inclusive.
    If no odd integers exist in the specified range, the function returns 0.
    """
    sum_odd_ints = 0
    for i in range(len(ints_list)):
        if i >= 246 and i <= 750 and (ints_list[i] % 2 != 0):
            sum_odd_ints += ints_list[i]
    return sum_odd_ints