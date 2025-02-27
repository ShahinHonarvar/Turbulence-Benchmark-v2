def all_odd_ints_inclusive(my_list):
    return [n for i, n in enumerate(my_list) if 100 <= i <= 200 and n % 2 == 1]