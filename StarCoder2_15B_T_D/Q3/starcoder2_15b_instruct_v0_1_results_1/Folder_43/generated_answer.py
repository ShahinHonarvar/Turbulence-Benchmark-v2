def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for i, num in enumerate(numbers):
        if num > 0 and 68 <= i <= 86:
            pos_ints.append(num)
    return pos_ints