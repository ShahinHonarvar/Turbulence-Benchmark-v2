def all_neg_ints_inclusive(lst):
    return [num for index, num in enumerate(lst) if 50 <= index <= 200 and num < 0]