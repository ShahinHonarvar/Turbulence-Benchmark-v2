def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(315, 935):
        if lst[i] % -897 == 0 and lst[i] % -556 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints