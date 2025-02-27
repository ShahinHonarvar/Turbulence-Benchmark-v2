def all_pos_ints_exclusive(numbers):
    result = []
    for i in range(3, 8):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result