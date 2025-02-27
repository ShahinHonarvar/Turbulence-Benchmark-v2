from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            while num > 0:
                if not isprime(num):
                    break
                num //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)