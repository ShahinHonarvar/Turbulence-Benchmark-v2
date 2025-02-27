from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[67]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = [n for n in range(x - 1, 1, -1) if is_right_truncatable_prime(n)]
    return sorted(result, reverse=True)