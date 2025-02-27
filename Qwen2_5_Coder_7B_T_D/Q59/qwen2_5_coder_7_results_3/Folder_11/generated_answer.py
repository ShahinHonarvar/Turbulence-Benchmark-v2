from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    limit = x
    left_truncatable_primes = []

    def is_left_truncatable(n):
        while n > 0:
            if n % 10 == 0 or not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, limit):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)