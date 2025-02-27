def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of `n` that are between 50 and 81, both inclusive.
    If no such divisors exist, returns 0.
    """
    sum_of_divisors = 0
    for i in range(50, 82):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors