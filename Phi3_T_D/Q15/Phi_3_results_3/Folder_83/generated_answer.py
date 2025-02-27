def sum_odd_ints_inclusive(integers):
    sum_odds = sum((num for num in integers[90:201] if num % 2 != 0))
    return sum_odds