def sum_of_divisors_in_range(n):
    """
    Returns the sum of all divisors of `n` between 15 and 92, inclusive.
    If no such divisors exist, returns 0.
    """
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 15 <= i <= 92:
            sum_of_divisors += i
    return sum_of_divisors