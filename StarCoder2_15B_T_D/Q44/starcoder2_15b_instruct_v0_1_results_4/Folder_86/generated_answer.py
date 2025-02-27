def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if i >= 43 and i <= 86 and is_composite_num(num)}

def is_composite_num(num):
    return num > 1 and any((num % i == 0 for i in range(2, num)))