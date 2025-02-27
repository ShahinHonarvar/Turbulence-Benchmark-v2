from itertools import product

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_primes(numbers):
    limit = numbers[24]
    primes = [int(''.join(map(str, p))) for p in product(range(1, 10), repeat=5) if is_prime(int(''.join(map(str, p))))]
    prime_set = set(primes)
    left_truncatables = []
    for prime in sorted(prime_set):
        if len(str(prime)) == 1 or all((int(str(prime)[i:]) in prime_set for i in range(1, len(str(prime))))):
            left_truncatables.append(prime)
    return [x for x in left_truncatables if x < limit]