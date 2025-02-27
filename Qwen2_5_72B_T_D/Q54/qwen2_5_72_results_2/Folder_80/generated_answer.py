def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes():
    primes = [2, 3, 5, 7]
    right_truncatable = []
    for prime in primes:
        next_primes = [10 * prime + i for i in range(1, 10, 2) if is_prime(10 * prime + i)]
        right_truncatable.extend(filter(lambda x: all((is_prime(int(str(x)[:i])) for i in range(1, len(str(x)) + 1))), next_primes))
        primes = next_primes
    return sorted(right_truncatable, reverse=True)

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    if x < 2:
        return []
    return [p for p in right_truncatable_primes() if p < x]