from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
            if not isprime(int(str(n)[:-i])):
                return False
        return isprime(n)
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)][::-1]