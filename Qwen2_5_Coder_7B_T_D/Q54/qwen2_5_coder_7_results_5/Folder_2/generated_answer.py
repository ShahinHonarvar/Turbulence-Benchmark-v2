from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[618]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)