def sum_odd_ints_inclusive(int_list):
    sum_odds = sum((num for num in int_list[0:3] if num % 2 != 0))
    return sum_odds