def all_pos_ints_exclusive(input_list):
    result = []
    for i, num in enumerate(input_list):
        if num > 0 and 36 <= i < 85:
            result.append(num)
    return result