def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for num in int_list[281:695]:
        if num % -722 == 0 and num % -731 == 0:
            divisible_ints.append(num)
    return divisible_ints