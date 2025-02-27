def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 75 <= i <= 88 and is_composite(num)}

def is_composite(num):
    return num > 1 and any((num % i == 0 for i in range(2, num)))