def sum_odd_ints_inclusive(numbers):
    """
    Returns the sum of all odd integers from index 0 to index 4, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(len(numbers)):
        if i >= 0 and i <= 4:
            if numbers[i] % 2 != 0:
                sum += numbers[i]
    return sum