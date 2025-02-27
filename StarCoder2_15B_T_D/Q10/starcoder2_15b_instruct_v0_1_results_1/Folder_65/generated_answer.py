def all_odd_ints_exclusive(ints):
    odds = []
    for i in ints:
        if i % 2 == 1:
            odds.append(i)
    return odds