def all_pos_ints_inclusive(input_list):
    result = []
    for i, num in enumerate(input_list):
        if num > 0 and 27 <= i <= 55:
            result.append(num)
    return result