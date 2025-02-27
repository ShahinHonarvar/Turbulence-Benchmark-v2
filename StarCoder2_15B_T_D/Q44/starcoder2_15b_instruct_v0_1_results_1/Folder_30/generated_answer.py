def composite_nums_between_indices(lst):
    return set(filter(lambda x: x > 1 and any((x % i == 0 for i in range(2, x))), lst[19:93]))