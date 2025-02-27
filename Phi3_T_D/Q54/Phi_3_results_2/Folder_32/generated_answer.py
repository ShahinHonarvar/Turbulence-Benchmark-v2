from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    truncatable_primes = []

    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n), 0, -1):
            if not isprime(int(n[:i])):
                return False
        return True
    for prime in range(2, x):
        if is_right_truncatable(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)