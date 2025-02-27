def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[8:10]:
        if num % -3 == 0 and num % 6 == 0:
            result.append(num)
    return result