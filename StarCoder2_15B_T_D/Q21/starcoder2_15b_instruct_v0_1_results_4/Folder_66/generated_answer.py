def all_ints_div_by_num(ints_list):
    divisible_ints = []
    for i in range(14, 69):
        if ints_list[i] % 18 == 0:
            divisible_ints.append(ints_list[i])
    return divisible_ints