def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[0:9]:
        if i % -3 == 0 and i % 8 == 0:
            result.append(i)
    return result