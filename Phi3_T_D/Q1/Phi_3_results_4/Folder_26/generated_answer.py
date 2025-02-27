def all_ints_inclusive(integers_list):
    try:
        return integers_list[50:55]
    except IndexError:
        return None