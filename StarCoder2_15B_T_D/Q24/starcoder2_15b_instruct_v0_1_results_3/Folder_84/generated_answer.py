def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of the given integer n that are between 224 and 584, both inclusive.
    If no such divisors exist, returns 0.
    """
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 224 <= i <= 584:
            sum += i
    return sum