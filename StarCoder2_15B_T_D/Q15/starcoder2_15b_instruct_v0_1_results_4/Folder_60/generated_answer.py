def sum_odd_ints_inclusive(ints):
    """
    Write a function called'sum_odd_ints_inclusive' that takes one argument,
    a list of integers, and returns the sum of all odd integers from index 75 to
    index 85, both inclusive. If no odd integers exist in the specified range, the
    function should return 0.
    """
    sum_odds = 0
    for i in range(75, 86):
        if ints[i] % 2 != 0:
            sum_odds += ints[i]
    return sum_odds