def sum_odd_ints_inclusive(list_of_ints):
    """
    Returns the sum of all odd integers from index 4 to index 8, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(4, 9):
        if list_of_ints[i] % 2 == 1:
            sum += list_of_ints[i]
    return sum