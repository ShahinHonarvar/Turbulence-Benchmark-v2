def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of n that are between 113 and 991, inclusive.
    If no such divisors exist, returns 0.
    """
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 113 <= i <= 991]
    return sum(divisors) if divisors else 0