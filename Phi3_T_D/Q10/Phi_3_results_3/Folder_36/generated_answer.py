def all_odd_ints_exclusive(ints_list):
    try:
        return [n for n in ints_list[598:767] if n % 2 != 0]
    except IndexError:
        return []