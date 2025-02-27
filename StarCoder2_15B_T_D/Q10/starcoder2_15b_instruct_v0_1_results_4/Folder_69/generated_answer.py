def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in range(68, 99):
        if i % 2 == 1:
            odd_ints.append(lst[i])
    return odd_ints