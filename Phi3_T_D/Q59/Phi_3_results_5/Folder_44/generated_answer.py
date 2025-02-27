def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, digits):
    while n > 0:
        n, last_digit = (n // 10, n % 10)
        if not is_prime(n) or last_digit == 0:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[39]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p, len(str(p)))]
    return left_truncatable_primes