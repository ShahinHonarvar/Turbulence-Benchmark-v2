from math import sqrt

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {item for item in lst[25:60] if is_composite(item)}