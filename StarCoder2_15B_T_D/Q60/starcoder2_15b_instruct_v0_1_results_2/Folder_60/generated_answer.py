def all_left_right_truncatable_prime(tup):
    """
    Return a list of all left-and-right-truncatable prime numbers less than or equal to x, where x is the 88th element of tup.
    """
    x = tup[87]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            left_trunc = int(str(i)[j:])
            right_trunc = int(str(i)[:-j - 1])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    """
    Return True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True