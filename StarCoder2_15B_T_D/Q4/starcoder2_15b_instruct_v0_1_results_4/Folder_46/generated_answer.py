def all_pos_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 20 < i < 43:
            result.append(num)
    return result