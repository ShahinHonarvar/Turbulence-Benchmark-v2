from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[630]

    def is_left_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i) and is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)