def all_left_right_truncatable_prime(numbers):
    """
    Returns a list of all left-and-right-truncatable prime numbers less than or equal to x,
    where x is the integer at index 975 in the given tuple of positive integers.
    """
    x = numbers[975]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, x + 1):
        is_left_truncatable_prime = True
        is_right_truncatable_prime = True
        j = i
        while j > 0:
            if not is_prime(j):
                is_left_truncatable_prime = False
                break
            j //= 10
        j = i
        while j > 0:
            if not is_prime(j):
                is_right_truncatable_prime = False
                break
            j %= 10 ** (len(str(j)) - 1)
        if is_left_truncatable_prime and is_right_truncatable_prime:
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    return sorted(left_truncatable_primes + right_truncatable_primes, reverse=True)

def is_prime(n):
    """
    Returns True if the given number is prime, False otherwise.
    """
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