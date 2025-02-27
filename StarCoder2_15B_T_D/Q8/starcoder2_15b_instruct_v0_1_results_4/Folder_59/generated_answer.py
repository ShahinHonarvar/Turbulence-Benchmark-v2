def all_even_ints_exclusive(ints):
    return [int for int in ints[0:10:2] if int % 2 == 0]