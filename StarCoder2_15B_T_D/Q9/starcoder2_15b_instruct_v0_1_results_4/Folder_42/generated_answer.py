def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i % 2 == 1 and 29 <= i <= 79]