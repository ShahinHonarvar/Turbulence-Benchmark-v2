def all_odd_ints_exclusive(ints):
    result = []
    for i in ints:
        if i % 2 == 1:
            result.append(i)
    return result