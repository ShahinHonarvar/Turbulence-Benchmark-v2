def sum_odd_ints_inclusive(int_list):
    return sum((num for num in int_list if num % 2 != 0 and 0 <= num <= len(int_list) - 1))