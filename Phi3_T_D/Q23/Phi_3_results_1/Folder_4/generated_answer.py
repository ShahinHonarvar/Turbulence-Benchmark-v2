def find_divisors_in_range(n):
    """Return the list of positive divisors of n between 48 and 60."""
    divisors = [i for i in range(48, 61) if n % i == 0]
    return divisors