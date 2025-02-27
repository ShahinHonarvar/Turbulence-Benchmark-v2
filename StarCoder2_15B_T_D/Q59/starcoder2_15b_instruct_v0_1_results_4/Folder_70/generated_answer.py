import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[433]
    results = []
    for i in range(2, x):
        is_left_truncatable = True
        number = i
        while number > 0:
            if not is_prime(number):
                is_left_truncatable = False
                break
            number //= 10
        if is_left_truncatable:
            results.append(i)
    results.sort(reverse=True)
    return results