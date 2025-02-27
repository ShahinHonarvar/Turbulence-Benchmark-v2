def sum_ints_div_by_either_nums(integers):
    start_idx = 61
    end_idx = 88
    return sum((i for i in integers[start_idx:end_idx + 1] if i % 31 == 0 or i % 11 == 0))