def all_odd_ints_inclusive(int_list):
    if len(int_list) < 557:
        return []
    return [x for x in int_list[209:557] if x % 2 != 0]