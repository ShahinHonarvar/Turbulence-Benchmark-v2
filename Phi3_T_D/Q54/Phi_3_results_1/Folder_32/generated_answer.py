def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    if n < 11:
        return []
    primes = []
    for p in range(11, n, 2):
        if is_prime(p):
            primes.append(p)
            if not any((p % i == 0 for i in primes)):
                continue
            break
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    primes = right_truncatable_primes(x)
    if not primes:
        return []
    return sorted([p for p in primes if all((is_prime(p // 10 ** i) for i in range(len(str(p)) - 1)))])