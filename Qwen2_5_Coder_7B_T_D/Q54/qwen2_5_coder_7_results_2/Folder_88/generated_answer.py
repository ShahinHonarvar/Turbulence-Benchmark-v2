from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[93]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            while num > 0 and isprime(num):
                num //= 10
            if num == 0:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)