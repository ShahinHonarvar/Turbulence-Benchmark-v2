def all_ints_div_by_num(lst):
    result = []
    for i in range(70, 72):
        if i < len(lst) and lst[i] % 85 == 0:
            result.append(lst[i])
    return result