from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[67]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n):
        while n:
            if not isprime(n):
                return False
            n = n // 10
        return True
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return right_truncatable_primes