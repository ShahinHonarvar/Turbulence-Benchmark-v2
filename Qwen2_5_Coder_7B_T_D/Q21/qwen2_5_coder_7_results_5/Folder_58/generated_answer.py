def all_ints_div_by_num(lst):
    return [num for index, num in enumerate(lst) if index >= 255 and index <= 618 and (num % 965 == 0)]