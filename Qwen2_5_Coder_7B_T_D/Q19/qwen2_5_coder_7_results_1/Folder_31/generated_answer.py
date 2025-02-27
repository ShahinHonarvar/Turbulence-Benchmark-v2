def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 18 < i < 38 and num % -67 != 0]