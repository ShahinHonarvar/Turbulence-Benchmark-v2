from sympy import primerange

def all_right_truncatable_prime(numbers):

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def is_right_truncatable_prime(n):
        return all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))
    x = numbers[11]
    truncable_primes = [p for p in primerange(2, x) if is_right_truncatable_prime(p)]
    return truncable_primes