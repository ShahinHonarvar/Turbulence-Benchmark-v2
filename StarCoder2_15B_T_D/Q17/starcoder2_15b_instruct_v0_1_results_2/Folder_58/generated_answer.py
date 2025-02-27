def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(240, 902):
        if int_list[i] % 546 == 0 and int_list[i] % 709 == 0:
            result.append(int_list[i])
    return result