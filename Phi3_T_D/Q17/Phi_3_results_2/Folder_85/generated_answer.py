def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for num in int_list[1:9]:
        if num % -9 == 0 and num % -3 == 0:
            divisible_by_both.append(num)
    return divisible_by_both