from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    left_trunc_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[i:]:
                return False
            if not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes)