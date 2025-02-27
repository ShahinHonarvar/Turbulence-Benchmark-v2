from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[758]

    def is_right_truncatable_prime(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)