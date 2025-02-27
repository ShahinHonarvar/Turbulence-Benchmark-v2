def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 78 and i <= 81 and (int_list[i] % 76 == 0) and (int_list[i] % 60 == 0):
            result.append(int_list[i])
    return result