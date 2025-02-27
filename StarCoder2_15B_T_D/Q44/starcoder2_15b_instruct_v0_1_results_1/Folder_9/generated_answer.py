def composite_nums_between_indices(lst):
    return set((num for num in lst[80:201] if any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))))