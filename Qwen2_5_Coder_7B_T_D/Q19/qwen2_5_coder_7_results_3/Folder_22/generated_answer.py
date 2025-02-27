def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 40 and i < 200 and (num % 71 != 0)]