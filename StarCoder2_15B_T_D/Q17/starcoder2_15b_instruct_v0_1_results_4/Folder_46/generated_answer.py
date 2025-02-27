def all_ints_div_by_both_two_nums(ints_list):
    divisible_ints = []
    for idx, num in enumerate(ints_list):
        if idx >= 11 and idx <= 46 and (num % 55 == 0) and (num % 36 == 0):
            divisible_ints.append(num)
    return divisible_ints