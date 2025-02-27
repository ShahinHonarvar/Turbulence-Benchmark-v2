def all_ints_div_by_num(lst):
    for i in range(70, 72):
        if lst[i] % 85 == 0:
            return [lst[i]]
    return []