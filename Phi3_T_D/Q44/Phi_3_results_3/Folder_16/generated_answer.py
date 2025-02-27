from math import sqrt

def composite_nums_between_indices(lst):
    min_index, max_index = (40, 80)
    composite_nums = {n for i, n in enumerate(lst[min_index:max_index + 1]) if n > 1 and any((n % i == 0 for i in range(2, int(sqrt(n)) + 1)))}
    return composite_nums