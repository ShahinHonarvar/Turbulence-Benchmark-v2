from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    right_trunc_primes = []

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable(num):
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)