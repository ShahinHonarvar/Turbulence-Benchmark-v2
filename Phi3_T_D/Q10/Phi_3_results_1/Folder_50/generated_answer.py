def all_odd_ints_exclusive(int_list):
    start, end = (70, 98)
    return [num for num in int_list[start:end] if num % 2 != 0]