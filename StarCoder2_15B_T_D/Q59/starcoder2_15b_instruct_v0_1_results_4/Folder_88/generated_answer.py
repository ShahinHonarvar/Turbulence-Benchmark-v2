import math

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]
    leading_digits = [str(i) for i in range(1, 10)]
    prime_numbers = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n == 0:
                return True
            if not is_prime(n):
                return False
        return False
    result = []
    for i in range(10, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)