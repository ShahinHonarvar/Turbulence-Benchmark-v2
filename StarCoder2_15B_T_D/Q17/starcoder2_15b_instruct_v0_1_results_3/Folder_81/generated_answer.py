def all_ints_div_by_both_two_nums(ints_list):
    return [num for num in ints_list[10:101] if num % 10 == 0 and num % 100 == 0]