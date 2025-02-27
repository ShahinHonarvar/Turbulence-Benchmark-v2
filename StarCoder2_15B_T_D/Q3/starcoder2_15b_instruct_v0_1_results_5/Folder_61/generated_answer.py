def all_pos_ints_inclusive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result