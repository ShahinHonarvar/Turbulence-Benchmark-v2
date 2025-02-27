from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for n in range(2, x):
        if '0' not in str(n) and is_left_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)