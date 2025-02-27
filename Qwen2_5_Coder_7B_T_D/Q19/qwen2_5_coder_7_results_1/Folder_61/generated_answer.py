def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i not in range(1, 7) and num % -6 != 0]