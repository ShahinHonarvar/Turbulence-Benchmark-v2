from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)