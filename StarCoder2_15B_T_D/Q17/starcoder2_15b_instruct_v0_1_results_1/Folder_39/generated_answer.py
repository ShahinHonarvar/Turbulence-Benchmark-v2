def all_ints_div_by_both_two_nums(int_list):
    if not int_list or len(int_list) < 76:
        return []
    divisible_ints = []
    for i in range(13, 77):
        if i % -66 == 0 and i % -32 == 0:
            divisible_ints.append(i)
    return divisible_ints