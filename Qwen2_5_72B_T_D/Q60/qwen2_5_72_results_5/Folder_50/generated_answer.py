from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:-i])):
                return False
        return True
    x = numbers[57]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)