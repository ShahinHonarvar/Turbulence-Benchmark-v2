def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable(n):
    original = str(n)
    if '0' in original:
        return False
    while len(original) > 1:
        if not is_prime(int(original)):
            return False
        original = original[1:-1]
    return is_prime(int(original)) if original else False

def all_left_right_truncatable_prime(t):
    x = t[466]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)