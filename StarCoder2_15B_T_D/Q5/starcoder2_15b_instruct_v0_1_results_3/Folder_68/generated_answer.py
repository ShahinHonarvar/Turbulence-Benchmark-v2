def all_neg_ints_inclusive(my_list):
    if len(my_list) < 9:
        return []
    neg_ints = []
    for i in range(9):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints