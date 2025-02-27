def is_composite(n):
    if n < 2 or n % 2 == 0:
        return n > 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers_list):
    return {num for num in numbers_list[51:87] if is_composite(num)}