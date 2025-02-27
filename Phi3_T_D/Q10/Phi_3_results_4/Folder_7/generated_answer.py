def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list[323:972], start=323) if x % 2 != 0]