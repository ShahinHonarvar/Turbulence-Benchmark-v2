import sympy

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if n < 10:
            return sympy.isprime(n)
        while n > 0:
            if not sympy.isprime(n) or '0' in str(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers[38]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)