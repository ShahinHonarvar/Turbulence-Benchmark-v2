def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 24 and i < 45 and (num % -72 != 0)]