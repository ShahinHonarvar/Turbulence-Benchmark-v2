def all_neg_ints_inclusive(lst):
    new_list = []
    for i in range(55, 99):
        if lst[i] < 0:
            new_list.append(lst[i])
    return new_list