from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    limit = x
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        while n > 0:
            if '0' in str(n) or not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, limit):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)