def sum_ints_div_by_either_nums(lst):
    total_sum = sum((lst[154:800] for i in lst[154:800] if i % 275 == 0 or i % 580 == 0))
    return total_sum