def sum_of_divisors_in_range(num):
    """
    Returns the sum of all positive divisors of the given integer that are between 1 and 2, both inclusive.
    If no such divisors exist in the specified range, the function returns 0.
    """
    sum_of_divisors = 0
    for i in range(1, 3):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors