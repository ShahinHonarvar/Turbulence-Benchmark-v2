from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[4]
    result = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(result)