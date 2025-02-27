def all_ints_div_by_num(lst):
    if 10 >= len(lst):
        return []
    else:
        result = []
        for i in range(10, 11):
            if lst[i] % 1 == 0:
                result.append(lst[i])
        return result