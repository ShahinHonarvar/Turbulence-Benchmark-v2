def all_pos_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num > 0 and 30 <= i < 200:
            result.append(num)
    return result