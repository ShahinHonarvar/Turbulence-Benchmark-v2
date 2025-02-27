from sympy import primerange, isprime

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    left_truncatable_primes = []
    primes = set(primerange(2, x))
    while primes:
        prime = primes.pop()
        if all((prime % 10 ** i in primes for i in range(len(str(prime))))):
            left_truncatable_primes.insert(0, prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes