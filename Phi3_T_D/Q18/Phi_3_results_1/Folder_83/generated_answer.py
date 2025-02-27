def sum_ints_div_by_either_nums(int_list):
    start, end = (90, 200)
    sum = 0
    for i in range(start, end + 1):
        if int_list[i] % -31 == 0 or int_list[i] % 13 == 0:
            sum += int_list[i]
    return sum