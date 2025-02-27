def all_ints_div_by_both_two_nums(intlist):
    divisible_ints = [num for num in intlist[250:630] if num % 850 == 0 and num % 587 == 0]
    return divisible_ints