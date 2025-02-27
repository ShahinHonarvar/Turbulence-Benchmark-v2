def composite_nums_between_indices(num_list):
    composites = set(filter(lambda num: num > 1 and (not all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))), num_list[22:24]))
    return composites