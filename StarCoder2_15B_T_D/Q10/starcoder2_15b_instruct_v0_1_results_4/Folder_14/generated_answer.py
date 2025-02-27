def all_odd_ints_exclusive(input_list):
    return [num for i, num in enumerate(input_list) if 1 <= i < 7 and num % 2 == 1]