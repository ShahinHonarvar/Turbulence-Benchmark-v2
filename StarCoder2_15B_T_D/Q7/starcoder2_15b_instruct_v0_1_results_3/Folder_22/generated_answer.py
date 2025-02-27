def all_even_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 40 and i <= 200 and (ints[i] % 2 == 0):
            result.append(ints[i])
    return result