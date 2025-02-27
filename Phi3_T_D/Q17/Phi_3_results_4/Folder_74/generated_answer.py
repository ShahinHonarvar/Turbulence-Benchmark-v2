def all_ints_div_by_both_two_nums(int_list):
    start_index = 90
    end_index = 97
    divisible_by_both = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % 13 == 0 and int_list[i] % 35 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both