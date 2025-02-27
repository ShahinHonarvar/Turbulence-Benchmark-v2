def all_pos_ints_exclusive(ints):
    results = []
    for i in ints:
        if i > 0 and 55 < i < 84:
            results.append(i)
    return results