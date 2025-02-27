import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    primes = [i for i in range(2, x + 1) if sympy.isprime(i) and '0' not in str(i)]
    left_right_truncatable = [p for p in primes if all((sympy.isprime(int(str(p)[:i])) for i in range(1, len(str(p))))) and all((sympy.isprime(int(str(p)[-i:])) for i in range(1, len(str(p)))))]
    return sorted(left_right_truncatable, reverse=True)