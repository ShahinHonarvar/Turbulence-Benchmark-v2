from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)