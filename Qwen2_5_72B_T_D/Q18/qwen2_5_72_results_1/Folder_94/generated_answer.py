def sum_ints_div_by_either_nums(lst):
    relevant_nums = lst[93:95]
    return sum((x for x in relevant_nums if x % -53 == 0 or x % -91 == 0))