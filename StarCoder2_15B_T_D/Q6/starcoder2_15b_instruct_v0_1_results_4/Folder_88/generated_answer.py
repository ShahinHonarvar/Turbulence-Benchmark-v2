def all_neg_ints_exclusive(ints_list):
    result = []
    for i in ints_list[2:8]:
        if i < 0:
            result.append(i)
    return result