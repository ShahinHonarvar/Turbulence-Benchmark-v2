def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i in range(8, 9):
        if ints[i] % 2 == 1:
            odd_ints.append(ints[i])
    return odd_ints