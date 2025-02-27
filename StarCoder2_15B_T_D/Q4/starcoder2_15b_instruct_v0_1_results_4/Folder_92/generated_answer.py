def all_pos_ints_exclusive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result