def all_odd_ints_inclusive(ints):
    result = []
    for i, n in enumerate(ints):
        if i >= 13 and i <= 68 and (n % 2 != 0):
            result.append(n)
    return result