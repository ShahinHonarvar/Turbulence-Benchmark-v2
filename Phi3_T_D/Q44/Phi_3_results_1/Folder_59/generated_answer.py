def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):

    def is_composite(x):
        return x > 1 and (not is_prime(x))
    return set(filter(is_composite, numbers[0:10]))