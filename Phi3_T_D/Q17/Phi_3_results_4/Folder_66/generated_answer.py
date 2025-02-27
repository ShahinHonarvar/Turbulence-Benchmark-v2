def all_ints_div_by_both_two_nums(int_list):
    start = 58
    end = 81
    return [x for x in int_list[start:end + 1] if x % 55 == 0 and x % 10 == 0]