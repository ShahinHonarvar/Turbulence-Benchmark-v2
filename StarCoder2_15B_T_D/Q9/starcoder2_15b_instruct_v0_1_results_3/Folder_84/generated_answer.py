def all_odd_ints_inclusive(ints_list):
    odd_ints = []
    for i in range(len(ints_list)):
        if i >= 43 and i <= 86 and (ints_list[i] % 2 != 0):
            odd_ints.append(ints_list[i])
    return odd_ints