from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    left_truncatables = []

    def is_left_truncatable_prime(n):
        if n < 10:
            return False
        tmp = n
        while tmp > 0:
            if not isprime(tmp):
                return False
            tmp = tmp % 10 ** (len(str(tmp)) - 1)
        return True
    for i in range(x - 1, 0, -1):
        if is_left_truncatable_prime(i):
            left_truncatables.append(i)
    return left_truncatables