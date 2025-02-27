def sum_ints_div_by_either_nums(lst):
    sum_of_ints = 0
    for i in range(200, 201):
        if lst[i] % 17 == 0 or lst[i] % -5 == 0:
            sum_of_ints += lst[i]
    return sum_of_ints