from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)