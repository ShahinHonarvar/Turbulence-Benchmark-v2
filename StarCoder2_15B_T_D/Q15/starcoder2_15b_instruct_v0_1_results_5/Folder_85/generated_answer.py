def sum_odd_ints_inclusive(numbers):
    """
    Returns the sum of all odd integers from index 6 to index 8, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd = 0
    for i in range(6, 9):
        if numbers[i] % 2 != 0:
            sum_odd += numbers[i]
    return sum_odd