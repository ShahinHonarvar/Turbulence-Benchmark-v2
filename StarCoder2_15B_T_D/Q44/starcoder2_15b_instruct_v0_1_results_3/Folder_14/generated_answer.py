def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 4 <= i <= 4 and num > 1 and (not all((num % d for d in range(2, int(num ** 0.5) + 1))))}