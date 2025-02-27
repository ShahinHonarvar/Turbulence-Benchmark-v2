def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, primes):
    if n not in primes:
        return False
    while n:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[945]
    primes = [i for i in range(2, x) if is_prime(i)]
    result = [p for p in primes if is_left_truncatable(p, primes)]
    return sorted(result, reverse=True)