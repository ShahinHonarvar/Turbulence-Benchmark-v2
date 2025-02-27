def all_pos_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num > 0 and i >= 0 and (i <= 5):
            result.append(num)
    return result