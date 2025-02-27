from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num = n
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        num = n
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)