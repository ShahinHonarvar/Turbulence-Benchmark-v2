from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((isprime(int(num[:i])) for i in range(1, len(num) + 1))):
            right_truncatable_primes.append(int(num))
    return sorted(right_truncatable_primes, reverse=True)