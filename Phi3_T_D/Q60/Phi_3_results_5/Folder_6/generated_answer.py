def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(primes_set, n, is_right_truncatable=False):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        if is_right_truncatable and len(s) == 1:
            return True
        if is_right_truncatable and (not is_prime(int(s[:-1]))):
            return False
        if not is_right_truncatable and (not is_prime(int(s[1:]))):
            return False
        s = s[:-1] if is_right_truncatable else s[1:]
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 74:
        x = numbers[74]
    else:
        x = numbers[74]
    primes_set = set((n for n in range(2, x + 1) if is_prime(n)))
    return [n for n in range(23, x + 1) if n in primes_set and is_truncatable(primes_set, n, True)]