import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[84]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if sympy.isprime(i) and all((sympy.isprime(int(i[1:])) for i in sympy.sievesieve((str(i), str(i)[1:-1])) if len(i[1:]) > 0)):
            left_truncatable_primes.append(i)
    return left_truncatable_primes