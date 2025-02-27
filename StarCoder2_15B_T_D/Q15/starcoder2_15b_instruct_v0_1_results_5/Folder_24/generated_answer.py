def sum_odd_ints_inclusive(numbers):
    """
    Returns the sum of all odd integers in the specified range (inclusive).
    If no odd integers exist, returns 0.
    """
    sum_of_odd_ints = 0
    for i in range(74, 96):
        if numbers[i] % 2 != 0:
            sum_of_odd_ints += numbers[i]
    return sum_of_odd_ints