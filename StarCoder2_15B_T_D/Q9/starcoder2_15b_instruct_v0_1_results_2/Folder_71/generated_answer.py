def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(len(ints)):
        if i >= 26 and i <= 52 and (ints[i] % 2 != 0):
            odd_ints.append(ints[i])
    return odd_ints