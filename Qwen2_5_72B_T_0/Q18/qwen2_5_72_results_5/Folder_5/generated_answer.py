def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[:2]:
        if num % -6 == 0 or num % 4 == 0:
            sum_nums += num
    return sum_nums