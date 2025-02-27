def all_left_truncatable_prime(x: tuple):
    """
    Returns a list of all left-truncatable prime numbers less than x.
    """
    x = x[6]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[j + 1:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True