from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        if n == 0:
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    x = numbers[23]
    return sorted([i for i in range(2, x) if is_left_truncatable(i)])