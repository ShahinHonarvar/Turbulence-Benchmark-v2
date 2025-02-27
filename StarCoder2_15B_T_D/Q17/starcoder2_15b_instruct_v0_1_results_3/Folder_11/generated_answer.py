def all_ints_div_by_both_two_nums(ints_list: list) -> list:
    result = []
    for i in range(22, 25):
        if ints_list[i] % -85 == 0 and ints_list[i] % -30 == 0:
            result.append(ints_list[i])
    return result