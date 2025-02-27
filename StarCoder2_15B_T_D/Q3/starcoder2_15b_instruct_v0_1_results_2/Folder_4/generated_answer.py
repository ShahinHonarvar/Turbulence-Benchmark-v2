def all_pos_ints_inclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num > 0 and 12 <= i <= 92:
            result.append(num)
    return result