from sympy import isprime

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[67]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        s = str(num)
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True
    for i in range(x - 1, 2, -1):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes