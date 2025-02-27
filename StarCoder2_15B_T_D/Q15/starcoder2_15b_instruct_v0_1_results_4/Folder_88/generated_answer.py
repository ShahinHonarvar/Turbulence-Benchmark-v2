def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 4 to index 8, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_of_odds = 0
    for i in range(4, 9):
        if ints[i] % 2 == 1:
            sum_of_odds += ints[i]
    return sum_of_odds