def all_odd_ints_exclusive(ints):
    odds = [i for i in ints if i % 2 == 1]
    return odds[2:5] if len(odds) >= 5 else []