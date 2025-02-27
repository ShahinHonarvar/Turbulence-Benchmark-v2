def all_pos_ints_exclusive(numbers):
    pos_ints = []
    for i, num in enumerate(numbers):
        if num > 0 and 87 <= i < 95:
            pos_ints.append(num)
    return pos_ints