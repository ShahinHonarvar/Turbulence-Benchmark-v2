def find_divisors_in_range(n):
    """Return a list of divisors of n that are in the range [16, 68]. """
    return [i for i in range(16, 69) if n % i == 0]