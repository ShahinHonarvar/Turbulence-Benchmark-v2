def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    start, end = (48, 76)
    for num in int_list[start:end + 1]:
        if num % -46 == 0 and num % -82 == 0:
            divisible_ints.append(num)
    return divisible_ints