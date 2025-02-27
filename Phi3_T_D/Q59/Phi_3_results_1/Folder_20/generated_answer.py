from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[100]
    truncatable_primes = []

    def is_left_truncatable(n, primes):
        str_n = str(n)
        if not all((char in '123456789' for char in str_n)):
            return False
        for i in range(len(str_n), 0, -1):
            if not isprime(int(str_n[:i])):
                return False
        return True
    for n in range(x - 1, 1, -1):
        if n < 10:
            truncatable_primes.append(n)
        elif isleft_truncatable(n, truncatable_primes):
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes