import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    left_truncatable = []

    def is_truncatable(n):
        if n < 10:
            return False
        while n > 0:
            if not sympy.isprime(n):
                return False
            n = n % (10 ** len(str(n)) // 10)
        return True
    for i in range(x - 1, 1, -1):
        if is_truncatable(i):
            left_truncatable.append(i)
    return left_truncatable