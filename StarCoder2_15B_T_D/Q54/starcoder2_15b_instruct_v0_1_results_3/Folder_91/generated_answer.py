def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    """
    Returns the sorted list of all right-truncatable prime numbers less than x.
    If there is no such right-truncatable prime number, returns an empty list.
    """
    if not isinstance(x, tuple) or len(x) != 1 or (not isinstance(x[0], int)) or (x[0] < 1):
        return []
    x = x[0]
    result = []
    for i in range(2, x):
        num = i
        while num < x:
            if not is_prime(num):
                break
            num //= 10
        if num == 0:
            result.append(i)
    return sorted(result, reverse=True)