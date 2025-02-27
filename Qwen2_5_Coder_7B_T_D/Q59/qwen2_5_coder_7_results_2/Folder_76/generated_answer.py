from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[370]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i + 1])) for i in range(len(num_str)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)