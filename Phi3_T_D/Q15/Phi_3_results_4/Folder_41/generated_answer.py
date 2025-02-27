def sum_odd_ints_inclusive(lst):
    start, end = (6, 6)
    sum_of_odds = sum(lst[start:end + 1:2] if lst[start] % 2 != 0 else [0])
    return sum_of_odds