def all_pos_ints_inclusive(numbers):
    positive_ints = filter(lambda x: x > 0, numbers)
    sliced_ints = positive_ints[80:201]
    return list(sliced_ints)