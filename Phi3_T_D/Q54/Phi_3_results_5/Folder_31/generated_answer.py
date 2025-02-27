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

def is_right_truncatable_prime(prime):
    return all((is_prime(int(prime[:i])) for i in range(1, len(str(prime)))))

def all_right_truncatable_prime(numbers_tup):
    x = numbers_tup[50]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [prime for prime in primes if is_right_truncatable_prime(prime)]
    return sorted(right_truncatable_primes, reverse=True)