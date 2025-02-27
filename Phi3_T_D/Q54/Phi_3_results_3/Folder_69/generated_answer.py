import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[760]
    right_truncatable_primes = []
    for i in range(3, x, 2):
        if sympy.isprime(i):
            s = str(i)
            while len(s) > 1:
                if sympy.isprime(int(s)):
                    s = s[:-1]
                else:
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)