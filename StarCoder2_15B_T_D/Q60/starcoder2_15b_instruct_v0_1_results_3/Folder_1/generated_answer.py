def all_left_right_truncatable_prime(numbers):
    """
    Find all left-and-right-truncatable prime numbers less than or equal to x.
    """
    x = numbers[20]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i))):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:len(str(i)) - j])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True