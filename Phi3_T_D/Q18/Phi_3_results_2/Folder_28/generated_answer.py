def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list[34:82], start=34) if num % 27 == 0 or num % 57 == 0))