def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_set = {num for num in lst[17:79] if is_composite(num)}
    return composite_set