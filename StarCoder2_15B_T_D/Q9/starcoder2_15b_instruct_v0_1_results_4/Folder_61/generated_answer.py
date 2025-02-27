def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(len(ints)):
        if i >= 0 and i <= 7:
            if ints[i] % 2 != 0:
                odd_ints.append(ints[i])
    return odd_ints