def all_ints_div_by_both_two_nums(ints_list):
    result = []
    for num in ints_list[55:85]:
        if num % -24 == 0 and num % -11 == 0:
            result.append(num)
    return result