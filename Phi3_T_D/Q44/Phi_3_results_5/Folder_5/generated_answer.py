def composite_nums_between_indices(lst):
    composite_set = {n for n in lst[1:6] if any((n % i == 0 for i in range(2, n))) and n != 1}
    return composite_set