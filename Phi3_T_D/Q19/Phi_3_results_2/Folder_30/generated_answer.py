def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[20:35]:
        if i % -36 != 0:
            result.append(i)
    return result