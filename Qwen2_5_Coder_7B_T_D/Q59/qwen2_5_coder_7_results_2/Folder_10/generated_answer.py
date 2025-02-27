from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatable_primes = []

    def is_left_truncatable(prime):
        while prime >= 10:
            prime //= 10
            if not isprime(prime) or '0' in str(prime):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)