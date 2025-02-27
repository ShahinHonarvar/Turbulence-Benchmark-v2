def composite_nums_between_indices(lst):
    return {x for x in lst[:3] if x >= 4 and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))}