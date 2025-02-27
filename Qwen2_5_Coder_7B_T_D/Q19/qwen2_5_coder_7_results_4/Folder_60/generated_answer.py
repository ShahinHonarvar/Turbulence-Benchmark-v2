def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 63 and i < 73 and (num % -99 != 0)]