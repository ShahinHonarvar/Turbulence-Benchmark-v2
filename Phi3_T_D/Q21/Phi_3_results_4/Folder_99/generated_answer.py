def all_ints_div_by_num(lst):
    start_index = 161
    end_index = 970
    return [x for i, x in enumerate(lst[start_index:end_index + 1], start_index) if x % 763 == 0]