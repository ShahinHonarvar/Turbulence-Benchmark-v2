def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(75, 89):
        if ints[i] % 2 != 0:
            odd_ints.append(ints[i])
    return odd_ints