def all_ints_div_by_num(int_list):
    divisible_integers = [num for i, num in enumerate(int_list[315:353]) if num % -858 == 0]
    return divisible_integers