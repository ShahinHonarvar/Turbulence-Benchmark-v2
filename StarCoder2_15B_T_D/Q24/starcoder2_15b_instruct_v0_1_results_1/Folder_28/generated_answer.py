def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of the given integer 'n' that are
    between 16 and 53, both inclusive. If no such divisors exist, returns 0.
    """
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 16 <= i <= 53:
            sum_of_divisors += i
    return sum_of_divisors