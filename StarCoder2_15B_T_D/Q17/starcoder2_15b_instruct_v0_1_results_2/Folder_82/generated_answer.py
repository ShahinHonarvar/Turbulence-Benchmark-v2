def all_ints_div_by_both_two_nums(ints):
    start_idx = ints.index(-20)
    end_idx = ints.index(-200)
    return [x for i, x in enumerate(ints) if i >= start_idx and i <= end_idx and (x % -20 == 0) and (x % -200 == 0)]