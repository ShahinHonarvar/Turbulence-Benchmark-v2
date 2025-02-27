def all_ints_div_by_both_two_nums(input_list):
    return [x for i, x in enumerate(input_list) if i in range(10) and all((x % n == 0 for n in (10, 100)))]