def all_ints_not_div_by_num(arg):
    if not isinstance(arg, list) or len(arg) < 7:
        return []
    results = []
    for i in range(4, 7):
        if arg[i] % -6 != 0:
            results.append(arg[i])
    return results