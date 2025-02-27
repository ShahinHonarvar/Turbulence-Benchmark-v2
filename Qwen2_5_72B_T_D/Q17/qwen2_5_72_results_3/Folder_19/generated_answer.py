def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[1:5]:
        if i % 4 == 0 and i % -6 == 0:
            result.append(i)
    return result