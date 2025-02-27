def all_odd_ints_exclusive(ints):
    result = []
    for i, x in enumerate(ints):
        if i >= 55 and i < 84 and (x % 2 == 1):
            result.append(x)
    return result