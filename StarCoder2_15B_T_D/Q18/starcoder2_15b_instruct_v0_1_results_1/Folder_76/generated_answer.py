def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(250, 630):
        if lst[i] % 850 == 0 or lst[i] % 587 == 0:
            sum += lst[i]
    return sum