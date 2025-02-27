def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if 21 < i < 69 and num % -69 != 0]