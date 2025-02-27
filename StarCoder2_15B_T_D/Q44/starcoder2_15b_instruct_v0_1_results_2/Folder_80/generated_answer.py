def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if i >= 62 and i <= 78 and (num > 1) and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1)))}