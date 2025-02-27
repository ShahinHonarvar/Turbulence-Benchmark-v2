def all_odd_ints_inclusive(int_list):
    start, end = (37, 52)
    return [num for num in int_list[start:end] if num % 2 != 0]