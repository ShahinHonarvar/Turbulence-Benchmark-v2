from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[94]

    def is_left_truncatable(n):
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return [n for n in range(2, x) if isprime(n) and '0' not in str(n) and is_left_truncatable(n)]