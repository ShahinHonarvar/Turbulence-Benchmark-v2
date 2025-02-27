def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 30 and i < 200 and (num % -115 != 0)]