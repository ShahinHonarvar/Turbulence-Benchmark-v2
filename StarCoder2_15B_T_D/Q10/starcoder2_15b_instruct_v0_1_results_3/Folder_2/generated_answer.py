def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(36, 52):
        if i % 2 == 1:
            odd_ints.append(int_list[i])
    return odd_ints