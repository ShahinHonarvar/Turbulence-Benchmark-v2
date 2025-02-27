def sum_ints_div_by_either_nums(int_list):
    start_idx, end_idx = (32, 99)
    if start_idx > len(int_list) or end_idx >= len(int_list):
        return 0
    return sum((x for x in int_list[start_idx:end_idx + 1] if x % -11 == 0 or x % -15 == 0))