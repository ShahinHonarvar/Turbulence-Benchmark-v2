def all_pos_ints_exclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if num > 0 and 361 <= i < 643:
            result.append(num)
    return result