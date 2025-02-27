def all_odd_ints_exclusive(ints):
    if len(ints) < 767:
        return []
    return [x for x in ints[598:767] if x % 2 != 0]