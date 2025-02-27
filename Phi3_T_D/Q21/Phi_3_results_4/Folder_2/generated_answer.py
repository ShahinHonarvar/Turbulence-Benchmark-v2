def all_ints_div_by_num(lst):
    start_index, end_index = (62, 70)
    return [num for num in lst[start_index:end_index + 1] if num % 58 == 0]