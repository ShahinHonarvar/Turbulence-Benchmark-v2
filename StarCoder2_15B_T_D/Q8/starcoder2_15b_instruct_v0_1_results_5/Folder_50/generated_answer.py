def all_even_ints_exclusive(int_list):
    if len(int_list) < 98:
        return []
    return [x for x in int_list[70:98] if x % 2 == 0]