import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((sympy.isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return left_truncatable_primes