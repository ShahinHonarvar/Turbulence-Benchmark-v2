def all_odd_ints_inclusive(ints):
    return [int for i, int in enumerate(ints) if i >= 20 and i <= 200 and (int % 2 == 1)]