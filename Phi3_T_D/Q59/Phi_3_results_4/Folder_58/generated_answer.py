from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes