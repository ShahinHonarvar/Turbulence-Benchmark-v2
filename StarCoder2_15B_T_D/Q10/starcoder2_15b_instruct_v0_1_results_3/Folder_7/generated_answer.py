def all_odd_ints_exclusive(ints):
    if len(ints) < 973:
        return []
    else:
        return ints[323:972:2]