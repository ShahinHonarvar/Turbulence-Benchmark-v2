def all_neg_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if num < 0 and 3 <= i <= 5]