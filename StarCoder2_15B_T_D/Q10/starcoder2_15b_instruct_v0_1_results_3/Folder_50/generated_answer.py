def all_odd_ints_exclusive(my_list):
    return [num for i, num in enumerate(my_list) if i >= 70 and i < 98 and (num % 2 == 1)]