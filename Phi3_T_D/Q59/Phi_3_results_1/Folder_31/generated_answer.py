def is_prime(n):
    if n <= 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

def left_truncatable_primes(n):

    def is_truncatable(n, primes):
        while n:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    primes = [p for p in range(2, n) if is_prime(p)]
    return [p for p in primes if is_truncatable(p, primes)]

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    return left_truncatable_primes(x)[::-1]