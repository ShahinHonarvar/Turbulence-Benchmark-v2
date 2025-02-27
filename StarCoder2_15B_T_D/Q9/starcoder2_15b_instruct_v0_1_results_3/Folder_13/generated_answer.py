def all_odd_ints_inclusive(my_list):
    return [num for i, num in enumerate(my_list) if i >= 25 and i <= 87 and (num % 2 != 0)]