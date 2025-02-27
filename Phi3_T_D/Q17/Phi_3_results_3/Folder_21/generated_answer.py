def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for i in int_list[315:935]:
        if i % -897 == 0 and i % -556 == 0:
            divisible_ints.append(i)
    return divisible_ints