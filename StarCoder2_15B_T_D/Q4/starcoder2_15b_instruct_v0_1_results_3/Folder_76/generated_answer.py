def all_pos_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num > 0 and 361 <= i < 643:
            result.append(num)
    return result