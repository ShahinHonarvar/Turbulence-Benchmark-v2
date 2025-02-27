from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            while num >= 10:
                num //= 10
                if not isprime(num):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)