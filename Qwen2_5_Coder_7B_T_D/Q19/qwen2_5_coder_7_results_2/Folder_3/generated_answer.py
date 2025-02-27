def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[31:69]) if num % -70 != 0]