def all_pos_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 86 <= i < 99:
            result.append(num)
    return result