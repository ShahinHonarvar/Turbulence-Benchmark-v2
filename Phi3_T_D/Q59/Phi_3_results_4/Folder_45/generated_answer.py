def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return n in primes

def all_left_truncatable_prime(numbers):
    n = numbers[61]
    primes = [i for i in range(2, n) if is_prime(i)]
    left_truncatable_primes = [p for p in primes if is_truncatable_prime(p, primes)]
    return left_truncatable_primes