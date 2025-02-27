def composite_nums_between_indices(lst):
    return {num for num in lst[74:96] if not all((num % i for i in range(2, int(num ** 0.5) + 1)))}