def sum_odd_ints_inclusive(lst):
    sum_odds = sum((n for n in lst[30:49] if n % 2 != 0))
    return sum_odds