def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for num in lst[34:70]:
        if num % 19 == 0 and num % 32 == 0:
            divisible_ints.append(num)
    return divisible_ints