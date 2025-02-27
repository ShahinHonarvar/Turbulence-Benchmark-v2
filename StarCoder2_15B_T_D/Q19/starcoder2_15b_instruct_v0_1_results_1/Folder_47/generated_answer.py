def all_ints_not_div_by_num(ints):
    spec_range = ints[25:76]
    result = []
    for i in spec_range:
        if i % -53 != 0:
            result.append(i)
    return result