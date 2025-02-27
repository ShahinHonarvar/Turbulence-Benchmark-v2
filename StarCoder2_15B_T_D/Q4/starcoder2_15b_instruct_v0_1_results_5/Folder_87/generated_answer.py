def all_pos_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num > 0 and 32 <= i < 99:
            result.append(num)
    return result