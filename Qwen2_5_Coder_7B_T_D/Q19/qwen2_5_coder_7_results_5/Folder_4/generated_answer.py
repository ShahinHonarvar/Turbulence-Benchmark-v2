def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 19 and i < 49 and (num % -36 != 0)]