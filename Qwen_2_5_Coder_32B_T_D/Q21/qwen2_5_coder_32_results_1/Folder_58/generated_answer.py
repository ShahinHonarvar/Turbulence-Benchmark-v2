def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 255 and i <= 618 and (x % 965 == 0)]