from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    res = []

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    for i in range(x - 1, 0, -1):
        if is_left_truncatable(i):
            res.append(i)
    return res