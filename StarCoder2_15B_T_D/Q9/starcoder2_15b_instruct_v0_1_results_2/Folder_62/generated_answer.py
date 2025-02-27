def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(91, 100):
        if ints[i] % 2 != 0:
            odd_ints.append(ints[i])
    return odd_ints