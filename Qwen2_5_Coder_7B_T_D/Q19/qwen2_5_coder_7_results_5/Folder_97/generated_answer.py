def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if 14 < i < 48 and num % 16 != 0]