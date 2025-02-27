def sum_odd_ints_inclusive(int_list):
    sum_odds = sum((d for d in int_list[37:77] if d % 2 != 0))
    return sum_odds