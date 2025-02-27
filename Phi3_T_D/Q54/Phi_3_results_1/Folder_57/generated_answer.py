import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if sympy.isprime(i) and all((sympy.isprime(i // 10 ** n % 10 ** (n + 1)) for n in range(len(str(i)) - 1))):
            truncatable_primes.append(i)
    return truncatable_primes