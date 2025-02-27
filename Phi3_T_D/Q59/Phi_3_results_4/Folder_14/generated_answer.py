from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    primes = [i for i in range(2, x) if isprime(i)]
    for prime in primes:
        if is_left_truncatable(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)