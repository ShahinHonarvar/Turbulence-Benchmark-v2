def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for num in lst[48:77]:
        if num % -46 == 0 or num % -82 == 0:
            total_sum += num
    return total_sum