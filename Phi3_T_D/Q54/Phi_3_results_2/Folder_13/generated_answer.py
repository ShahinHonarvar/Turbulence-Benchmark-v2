def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(prime, primes):
    while prime > 0:
        prime = int(str(prime)[:-1])
        if prime not in primes:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[784]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    return sorted([int(p) for p in primes if is_right_truncatable(int(p), primes)])