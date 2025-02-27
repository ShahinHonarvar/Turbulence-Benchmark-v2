def all_pos_ints_inclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 13 <= i <= 68:
            result.append(num)
    return result