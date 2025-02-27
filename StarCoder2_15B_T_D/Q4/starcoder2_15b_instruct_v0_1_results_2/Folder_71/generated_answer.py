def all_pos_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num > 0 and 36 <= i < 54:
            result.append(num)
    return result