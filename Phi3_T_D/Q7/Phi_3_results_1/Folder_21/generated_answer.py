def all_even_ints_inclusive(int_list):
    if len(int_list) < 976:
        return []
    return [x for x in int_list[639:976] if x % 2 == 0]