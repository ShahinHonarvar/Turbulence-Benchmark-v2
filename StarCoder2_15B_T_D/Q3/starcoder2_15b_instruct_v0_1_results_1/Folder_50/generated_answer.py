def all_pos_ints_inclusive(numbers):

    def is_positive(x):
        return x > 0
    return list(filter(is_positive, numbers[70:85]))