from sympy import primerange, isprime

def all_left_truncatable_prime(numbers):
    if len(numbers) < 15:
        raise ValueError('Tuple must contain at least 15 elements.')
    x = numbers[14]
    primes = list(primerange(10, x))
    left_truncatables = [p for p in primes if all((isprime(int(str(p)[i:])) for i in range(len(str(p)))))]
    return sorted(left_truncatables, reverse=True)