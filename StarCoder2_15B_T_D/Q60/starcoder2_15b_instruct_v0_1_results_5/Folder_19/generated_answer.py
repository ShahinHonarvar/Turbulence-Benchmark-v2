def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable_prime(n % 10 ** (len(str(n)) - 1))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    if not isinstance(tup, tuple) or not all((isinstance(x, int) and x > 0 for x in tup)):
        raise TypeError('Invalid input. Expected a tuple of positive integers.')
    x = tup[67]
    return sorted(filter(is_truncatable_prime, range(x + 1)), reverse=True)