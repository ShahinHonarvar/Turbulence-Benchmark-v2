def all_ints_div_by_num(ints):
    return [int for i, int in enumerate(ints) if i >= 62 and i <= 70 and (int % 58 == 0)]