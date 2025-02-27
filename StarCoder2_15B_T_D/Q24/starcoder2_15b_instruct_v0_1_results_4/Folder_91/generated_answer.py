def sum_of_divisors_in_range(num):
    """
    Returns the sum of all positive divisors of the given integer that are between 2 and 9, both inclusive.
    If no such divisors exist in the specified range, returns 0.
    """
    divisors_sum = 0
    for i in range(2, 10):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum