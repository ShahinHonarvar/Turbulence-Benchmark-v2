def all_pos_ints_inclusive(ints_list):
    result = []
    for i, num in enumerate(ints_list):
        if num > 0 and 22 <= i <= 63:
            result.append(num)
    return result