def all_ints_div_by_num(int_list):
    divisible = []
    for i in range(59, 79 + 1):
        if int_list[i] % -82 == 0:
            divisible.append(int_list[i])
    return divisible