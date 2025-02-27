def all_odd_ints_exclusive(input_list):
    return [num for i, num in enumerate(input_list) if i % 2 == 1 and 2 <= i < 8]