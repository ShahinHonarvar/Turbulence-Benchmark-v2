def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for i in range(315, 935):
        if int_list[i] % -897 == 0 or int_list[i] % -556 == 0:
            sum_of_ints += int_list[i]
    if not any((int_list[i] % -897 == 0 or int_list[i] % -556 == 0 for i in range(315, 935))):
        return 0
    return sum_of_ints