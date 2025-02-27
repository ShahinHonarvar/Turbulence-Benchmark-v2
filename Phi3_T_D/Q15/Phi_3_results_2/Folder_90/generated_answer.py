def sum_odd_ints_inclusive(int_list):
    start, end = (262, 746)
    sum_of_odds = sum((num for idx, num in enumerate(int_list[start:end + 1]) if num % 2 != 0))
    return sum_of_odds