from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return isprime(n)
    for num in range(2, x):
        if str(num).count('0') == 0 and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)