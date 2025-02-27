def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of the given integer that are between 6 and 9, both inclusive.
    If no such divisors exist in the specified range, the function should return 0.
    """
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 6 <= i <= 9:
            sum_of_divisors += i
    return sum_of_divisors