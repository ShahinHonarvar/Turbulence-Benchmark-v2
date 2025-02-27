from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[35]
    result = []
    for num in range(x - 1, 1, -1):
        if is_right_truncatable_prime(num):
            result.append(num)
    return result