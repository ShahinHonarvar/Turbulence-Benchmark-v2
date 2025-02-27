def all_odd_ints_exclusive(lst):
    result = []
    for i in range(10, 12):
        if i < len(lst) and lst[i] % 2 != 0:
            result.append(lst[i])
    return result