def sum_odd_ints_inclusive(ints_list):
    sum_odds = sum((ints_list[74:96][i] for i in range(len(ints_list[74:96])) if ints_list[74:96][i] % 2 != 0))
    return sum_odds