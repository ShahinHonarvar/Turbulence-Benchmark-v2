from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[630]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result, reverse=True)