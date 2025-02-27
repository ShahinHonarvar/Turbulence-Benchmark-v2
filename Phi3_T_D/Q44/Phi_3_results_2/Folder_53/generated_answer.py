def is_composite(n):
    return n > 3 and any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))

def composite_nums_between_indices(lst):
    return set(filter(is_composite, lst[222:223]))