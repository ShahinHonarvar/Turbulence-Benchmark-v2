def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if 7 < i < 9 and num % -9 != 0]