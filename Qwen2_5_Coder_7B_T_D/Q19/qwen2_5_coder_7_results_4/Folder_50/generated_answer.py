def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 13 < i < 76 and num % 44 != 0]