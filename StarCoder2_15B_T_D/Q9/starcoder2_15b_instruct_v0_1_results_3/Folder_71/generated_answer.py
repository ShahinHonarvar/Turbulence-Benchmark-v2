def all_odd_ints_inclusive(ints):
    try:
        return [i for i in ints[26:53] if i % 2 != 0]
    except Exception as e:
        return []