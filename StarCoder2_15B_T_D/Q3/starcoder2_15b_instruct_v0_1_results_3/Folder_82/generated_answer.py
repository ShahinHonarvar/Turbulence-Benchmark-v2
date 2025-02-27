def all_pos_ints_inclusive(list_of_ints):
    pos_ints = []
    for i, num in enumerate(list_of_ints):
        if num > 0 and 20 <= i <= 200:
            pos_ints.append(num)
    return pos_ints