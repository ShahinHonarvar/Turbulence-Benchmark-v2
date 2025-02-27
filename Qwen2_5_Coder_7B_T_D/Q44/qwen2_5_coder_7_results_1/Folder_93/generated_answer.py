def composite_nums_between_indices(lst):
    return set(filter(lambda x: x > 1 and any((x % i == 0 for i in range(2, int(x ** 0.5) + 1))), lst[23:24]))