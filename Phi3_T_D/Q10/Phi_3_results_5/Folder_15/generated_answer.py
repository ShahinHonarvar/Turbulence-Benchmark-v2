def all_odd_ints_exclusive(integer_list):
    filtered_odds = [num for num in integer_list[0:3] if num % 2 != 0]
    return filtered_odds