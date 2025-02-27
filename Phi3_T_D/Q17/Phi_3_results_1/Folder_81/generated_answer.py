def all_ints_div_by_both_two_nums(lst):
    return [number for number in lst[10:101] if number % 10 == 0 and number % 100 == 0]