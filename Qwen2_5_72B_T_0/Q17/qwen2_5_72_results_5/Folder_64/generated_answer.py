def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[:4]:
        if num % 11 == 0 and num % -7 == 0:
            result.append(num)
    return result