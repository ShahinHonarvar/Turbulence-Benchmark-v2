def all_pos_ints_inclusive(input_list):
    result = []
    for i, num in enumerate(input_list):
        if num > 0 and 40 <= i <= 80:
            result.append(num)
    return result