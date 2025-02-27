def all_pos_ints_exclusive(numbers):
    pos_ints = []
    for i in range(2, 7):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints