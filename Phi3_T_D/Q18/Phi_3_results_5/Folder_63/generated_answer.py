def sum_ints_div_by_either_nums(lst):
    summation = 0
    for num in lst[31:51]:
        if num % 81 == 0 or num % 64 == 0:
            summation += num
    return summation