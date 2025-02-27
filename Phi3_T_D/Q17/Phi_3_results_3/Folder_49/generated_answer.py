def all_ints_div_by_both_two_nums(lst):
    return [val for val in lst[80:201] if val % 10 == 0 and val % 1000 == 0]