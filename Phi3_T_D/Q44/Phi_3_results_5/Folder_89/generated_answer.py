from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    comps = {num for num in numbers[36:47] if not is_prime(num)}
    return comps