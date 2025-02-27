from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    right_truncatable_primes = []

    def is_right_truncatable(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)