def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(62, 93):
        if ints[i] % 2 == 1:
            odd_ints.append(ints[i])
    return odd_ints