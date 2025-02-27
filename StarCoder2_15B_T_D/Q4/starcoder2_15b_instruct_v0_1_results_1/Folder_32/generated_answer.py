def all_pos_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 11 <= i < 76:
            result.append(num)
    return result