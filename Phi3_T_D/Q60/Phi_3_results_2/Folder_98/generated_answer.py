def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    truncable_primes = []
    digits = [str(i) for i in range(1, 10)]

    def is_truncatable_prime(prime, ldiv, rdiv):
        for d in digits:
            if not is_prime(int(d + prime)):
                return False
            prime = d + prime[1:]
        for d in reversed(digits):
            if not is_prime(int(prime + d)):
                return False
            prime = prime[:-1] + d
        return True
    for prime in range(11, x + 1, 2):
        if is_prime(prime) and is_truncatable_prime(str(prime), '', ''):
            truncable_primes.append(prime)
    return sorted(truncable_primes, reverse=True)