def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(list_of_ints):
    return {num for idx, num in enumerate(list_of_ints[42:69]) if not is_prime(num)}