def all_ints_div_by_both_two_nums(lst):
    start = 51
    end = 76
    result = [x for x in lst[start:end + 1] if x % -90 == 0 and x % -59 == 0]
    return result