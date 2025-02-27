def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[945]
    primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(primes, reverse=True)