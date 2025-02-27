def all_pos_ints_inclusive(numbers):
    pos_ints = [num for num in numbers if num > 0]
    if len(pos_ints) > 98:
        return pos_ints[55:100]
    else:
        return pos_ints[55:]