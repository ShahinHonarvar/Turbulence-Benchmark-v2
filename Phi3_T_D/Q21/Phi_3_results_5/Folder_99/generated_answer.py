def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers[161:971], start=161) if num % 763 == 0]