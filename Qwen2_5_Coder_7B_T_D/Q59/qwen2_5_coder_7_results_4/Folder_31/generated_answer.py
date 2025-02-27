from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)