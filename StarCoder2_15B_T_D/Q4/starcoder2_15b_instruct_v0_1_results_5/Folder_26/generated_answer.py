def all_pos_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 44 < i < 78:
            result.append(num)
    return result