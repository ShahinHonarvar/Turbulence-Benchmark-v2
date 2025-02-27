def all_pos_ints_exclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if num > 0 and 55 <= i < 84:
            result.append(num)
    return result