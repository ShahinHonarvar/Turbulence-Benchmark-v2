def all_pos_ints_inclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 43 <= i <= 51:
            result.append(num)
    return result