from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        while n > 0:
            if '0' in str(n) or not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)