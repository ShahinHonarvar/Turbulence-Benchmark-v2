from sympy import isprime

def all_right_truncatable_prime(numbers):

    def right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[37]
    result = [n for n in range(2, x) if right_truncatable_prime(n)]
    return sorted(result, reverse=True)