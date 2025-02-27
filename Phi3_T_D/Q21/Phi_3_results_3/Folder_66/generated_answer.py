def all_ints_div_by_num(lst):
    start = 14
    end = 68
    if len(lst) < end:
        return []
    return [num for num in lst[start:end + 1] if num % 18 == 0]