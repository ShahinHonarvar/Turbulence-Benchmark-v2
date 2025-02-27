def all_ints_div_by_both_two_nums(int_list):
    both_divisible = []
    for index in range(240, 902):
        num = int_list[index]
        if num % 546 == 0 and num % 709 == 0:
            both_divisible.append(num)
    return both_divisible