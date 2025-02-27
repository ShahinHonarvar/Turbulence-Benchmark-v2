def all_ints_div_by_num(ints_list):
    divisible_ints = []
    for i in range(40, 401):
        if ints_list[i] % 7 == 0:
            divisible_ints.append(ints_list[i])
    return divisible_ints