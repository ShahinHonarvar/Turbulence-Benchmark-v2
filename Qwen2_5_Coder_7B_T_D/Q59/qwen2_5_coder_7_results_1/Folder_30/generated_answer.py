from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[37]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    primes = [i for i in range(2, x) if isprime(i) and is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)