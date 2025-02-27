def all_pos_ints_inclusive(numbers):
    numbers.sort()
    pos_ints = [num for num in numbers if num > 0]
    return pos_ints[28:33]