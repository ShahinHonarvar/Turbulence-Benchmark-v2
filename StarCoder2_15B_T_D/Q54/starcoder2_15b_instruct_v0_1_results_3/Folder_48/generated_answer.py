def all_right_truncatable_prime(numbers):
    """
    Returns a sorted list of all right-truncatable prime numbers less than
    numbers[835].
    """
    x = numbers[835]
    truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True