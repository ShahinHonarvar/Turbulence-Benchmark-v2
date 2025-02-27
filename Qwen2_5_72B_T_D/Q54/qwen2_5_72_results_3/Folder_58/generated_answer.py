from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[975]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = []
    for num in range(2, x):
        if isprime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)