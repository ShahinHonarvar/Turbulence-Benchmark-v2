def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    if not n in primes and (not is_prime(n)):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[93]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    while primes[-1] < x:
        primes.append(next((p for p in range(primes[-1] + 1, 10 * primes[-1]) if is_prime(p))))
    for prime in primes:
        if prime < x and is_right_truncatable_prime(prime, set(primes)):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)