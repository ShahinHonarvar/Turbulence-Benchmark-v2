from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    primes = []
    for num in range(2, x):
        if all((isprime(int(num[:i])) for i in range(1, len(num) + 1))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes)