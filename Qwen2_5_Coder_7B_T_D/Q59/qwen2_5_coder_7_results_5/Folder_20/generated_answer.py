from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and all((isprime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)