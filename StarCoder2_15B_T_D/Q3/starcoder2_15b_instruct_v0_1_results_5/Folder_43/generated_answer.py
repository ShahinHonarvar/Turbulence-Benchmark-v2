def all_pos_ints_inclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 68 <= i <= 86:
            result.append(num)
    return result