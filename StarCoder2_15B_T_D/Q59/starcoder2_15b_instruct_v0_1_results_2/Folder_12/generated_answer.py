import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    all_candidates = itertools.permutations(range(1, 10), len(str(x)))
    left_truncatable_primes = filter(is_prime, (int(''.join(map(str, c))) for c in all_candidates))
    return sorted(left_truncatable_primes, reverse=True)