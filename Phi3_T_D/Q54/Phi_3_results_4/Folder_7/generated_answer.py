def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, prime_list):
    return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1)))

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
    return sorted(right_truncatable_primes)