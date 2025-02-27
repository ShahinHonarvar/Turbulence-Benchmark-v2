def composite_nums_between_indices(lst):
    return {x for x in lst[639:976] if not all((x % i for i in range(2, int(x ** 0.5) + 1)))}