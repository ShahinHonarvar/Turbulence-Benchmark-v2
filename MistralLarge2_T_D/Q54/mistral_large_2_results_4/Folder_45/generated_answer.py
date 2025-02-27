from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    primes = []

    def is_right_truncatable_prime(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)