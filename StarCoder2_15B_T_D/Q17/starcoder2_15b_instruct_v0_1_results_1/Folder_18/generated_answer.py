def all_ints_div_by_both_two_nums(ints_list):
    divisible_ints = []
    for i in range(5, 6 + 1):
        if ints_list[i] % 22 == 0 and ints_list[i] % 82 == 0:
            divisible_ints.append(ints_list[i])
    return divisible_ints