from sympy import isprime

def is_left_truncatable_prime(n):
    while n:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    left_truncatable_primes = []
    for number in range(x - 1, 25, -1):
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes