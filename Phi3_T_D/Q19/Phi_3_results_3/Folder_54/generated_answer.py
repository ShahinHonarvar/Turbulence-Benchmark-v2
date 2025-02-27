def all_ints_not_div_by_num(lst):
    start = 19
    end = 94
    return [num for num in lst[start:end] if num % -32 != 0]