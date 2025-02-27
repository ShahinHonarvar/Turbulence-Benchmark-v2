def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i in range(59, 93):
        if ints[i] % 2 != 0:
            odd_ints.append(ints[i])
    return odd_ints