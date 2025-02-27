def sum_ints_div_by_either_nums(int_list):
    sum_result = 0
    for index in range(90, 98):
        if int_list[index] % 13 == 0 or int_list[index] % 35 == 0:
            sum_result += int_list[index]
    return sum_result