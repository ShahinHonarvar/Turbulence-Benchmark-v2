from sympy import isprime

def all_left_truncatable_prime(tpl):
    x = tpl[174]
    left_truncatable_primes = []

    def is_left_truncatable_prime(number):
        if not isprime(number):
            return False
        while number > 0:
            number = number % 10 ** (len(str(number)) - 1)
            if not isprime(number):
                return False
        return True
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes