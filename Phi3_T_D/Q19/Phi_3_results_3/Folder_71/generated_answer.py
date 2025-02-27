def all_ints_not_div_by_num(int_lst):
    start_idx = 21
    end_idx = 51
    return [num for num in int_lst[start_idx:end_idx] if num % -77 != 0]