from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    truncatable_primes = []

    def is_left_truncatable_prime(n):
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)