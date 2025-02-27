def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, prime_set):
    """Check if n is a left-truncatable prime number."""
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    result = []
    prime_set = set()
    for p in range(x - 1, 1, -1):
        if is_prime(p) and p not in prime_set and is_left_truncatable(p, prime_set):
            result.append(p)
            for i in range(1, len(str(p))):
                prime_set.add(int(str(p)[i:]))
    return result