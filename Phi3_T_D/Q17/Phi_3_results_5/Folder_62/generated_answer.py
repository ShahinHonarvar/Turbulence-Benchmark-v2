def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 60:
        return []
    divisible_ints = []
    for i in range(44, 60):
        if int_list[i] % 39 == 0 and int_list[i] % 15 == 0:
            divisible_ints.append(int_list[i])
    return divisible_ints