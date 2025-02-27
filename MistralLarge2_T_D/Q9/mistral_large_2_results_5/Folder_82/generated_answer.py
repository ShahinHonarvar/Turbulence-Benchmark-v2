def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if 20 <= i <= 200 and num % 2 != 0]