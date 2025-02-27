def find_divisors_in_range(num):
    """Finds all positive divisors of 'num' that are between 59 and 88, both inclusive."""
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and 59 <= i <= 88:
            divisors.append(i)
    return divisors