def all_odd_ints_inclusive(ints_list):
    odd_ints = []
    for i in ints_list:
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints