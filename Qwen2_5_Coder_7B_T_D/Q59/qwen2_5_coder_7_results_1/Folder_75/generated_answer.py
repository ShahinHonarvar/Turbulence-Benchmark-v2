from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i])) for i in range(1, len(num_str) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)