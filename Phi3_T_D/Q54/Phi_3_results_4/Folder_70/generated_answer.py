from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[433]
    truncable_primes = []

    def is_right_truncatable(prime):
        str_prime = str(prime)
        while len(str_prime) > 1:
            if not isprime(int(str_prime)):
                return False
            str_prime = str_prime[:-1]
        return True
    for n in range(x - 1, 1, -1):
        if isprime(n) and is_right_truncatable(n):
            truncable_primes.append(n)
    return truncable_primes