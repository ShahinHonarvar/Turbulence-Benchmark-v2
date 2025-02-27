def all_ints_not_div_by_num(lst):
    start, end = (84, 86)
    return [num for num in lst[start:end] if num % 99 != 0]