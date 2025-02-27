import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[57]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not sympy.isprime(n):
                return False
            n //= 10
        return True
    result = [i for i in range(x - 1, 1, -1) if is_right_truncatable_prime(i)]
    return result