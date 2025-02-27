def all_odd_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if i % 2 == 1 and 0 <= i <= 7:
            result.append(ints[i])
    return result