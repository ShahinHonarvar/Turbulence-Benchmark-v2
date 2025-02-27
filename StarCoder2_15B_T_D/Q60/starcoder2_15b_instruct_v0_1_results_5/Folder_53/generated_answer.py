def all_left_right_truncatable_prime(x):
    """
    This function takes a tuple of positive integers and returns a list of all left-and-right-truncatable prime numbers less than or equal to the integer at index 86.
    """
    x = x[86]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j + 1:])
            right_truncation = int(str(i)[:len(str(i)) - j - 1])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True