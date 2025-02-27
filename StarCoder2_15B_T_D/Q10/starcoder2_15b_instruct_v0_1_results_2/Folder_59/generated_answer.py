def all_odd_ints_exclusive(ints):
    return [int for int in ints if int % 2 == 1][0:10:2]