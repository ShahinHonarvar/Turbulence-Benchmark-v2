def all_ints_div_by_num(ints_list):
    divisible_ints = []
    for i in range(59, 80):
        if ints_list[i] % -82 == 0:
            divisible_ints.append(ints_list[i])
    return divisible_ints