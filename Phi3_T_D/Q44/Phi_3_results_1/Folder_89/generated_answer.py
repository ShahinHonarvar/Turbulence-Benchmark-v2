def composite_nums_between_indices(lst):
    composite_numbers = set()
    for num in lst[36:47]:
        if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_numbers.add(num)
    return composite_numbers