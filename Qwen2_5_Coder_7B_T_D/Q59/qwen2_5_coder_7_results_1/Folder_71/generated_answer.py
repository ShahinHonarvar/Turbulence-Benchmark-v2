from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[22]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num))))) and '0' not in str(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)