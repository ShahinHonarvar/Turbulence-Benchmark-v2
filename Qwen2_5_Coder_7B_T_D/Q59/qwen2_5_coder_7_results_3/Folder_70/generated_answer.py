import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    left_truncatable_primes = []
    for num in range(2, x):
        if str(num).count('0') == 0 and all((sympy.isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)