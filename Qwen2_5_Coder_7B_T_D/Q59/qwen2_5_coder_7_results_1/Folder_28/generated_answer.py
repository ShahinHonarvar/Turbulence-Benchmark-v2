from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    primes = []
    for num in range(2, x):
        if all((isprime(int(num[:i])) for i in range(1, len(num)))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes)