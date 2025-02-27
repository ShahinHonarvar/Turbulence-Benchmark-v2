def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst[26:91], start=27) if num % 57 == 0]