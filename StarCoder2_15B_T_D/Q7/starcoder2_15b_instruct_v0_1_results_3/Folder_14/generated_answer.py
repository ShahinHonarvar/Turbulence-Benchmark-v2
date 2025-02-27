def all_even_ints_inclusive(ints):
    output = []
    for i in range(5, 8):
        if ints[i] % 2 == 0:
            output.append(ints[i])
    return output