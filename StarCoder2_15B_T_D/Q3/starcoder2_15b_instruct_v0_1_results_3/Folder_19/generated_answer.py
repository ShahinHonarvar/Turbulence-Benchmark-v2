def all_pos_ints_inclusive(numbers):
    result = []
    for i in range(3, 6):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result