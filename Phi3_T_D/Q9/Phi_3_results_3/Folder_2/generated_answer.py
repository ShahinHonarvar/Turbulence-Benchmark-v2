def all_odd_ints_inclusive(int_list):
    start, end = (15, 39)
    return [num for num in int_list[start:end + 1] if num % 2 != 0]